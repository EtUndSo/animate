import numpy as np
from .constants import PIXEL_WIDTH, PIXEL_HEIGHT, FRAME_HEIGHT, RIGHT, UP


class Camera:
    """Maps 3D world points to 2D pixel coordinates - the single place that knows about PROJECTION.

    2D mode: orthographic onto RIGHT/UP (depth dropped) - unchanged.

    3D mode: a Z-UP orbit camera (like GeoGebra 3D / Manim's ThreeDAxes). The world z-axis points
    STRAIGHT UP on screen; x and y span the horizontal ground plane. The camera sits on a sphere
    around the origin given by
        theta = azimuth, spins horizontally around the vertical z-axis,
        phi   = elevation above the ground plane (phi -> pi/2 looks straight down from the top).
    We build an orthonormal camera frame with a genuine "look-at" so that world-up (+z) ALWAYS maps
    to screen-up: screen_x = right-component, screen_y = up-component, depth = component towards the
    camera (larger = nearer -> drawn on top). Perspective/zoom can be added here later without
    touching anything else.

    Performance: projection is available BATCHED (view_array / project_array over an (N,3) array) so
    the renderer can transform a whole surface mesh in ONE numpy matmul instead of a Python-level call
    per point - the same trick that makes mpl3d-turbo ~5-10x faster than matplotlib's mplot3d, which
    (like us) is a painter's-algorithm renderer with no GPU.
    """

    def __init__(self, pixel_width=PIXEL_WIDTH, pixel_height=PIXEL_HEIGHT, frame_height=FRAME_HEIGHT,
                 mode="2d", theta=0.6, phi=1.0, zoom=1.0):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height
        self.units_per_pixel = frame_height / pixel_height
        self.mode = mode
        self.zoom = float(zoom) or 1.0        # orthographic zoom: >1 = closer (world looks bigger)
        self.orient(theta, phi)

    @property
    def _upp(self):
        """Effective units-per-pixel after zoom (smaller -> the world is magnified)."""
        return self.units_per_pixel / self.zoom

    def orient(self, theta, phi):
        """Set the orbit angles (radians) and cache the camera-frame rotation matrix (z-up look-at)."""
        self.theta = float(theta)
        self.phi = float(phi)
        ct, st = np.cos(self.theta), np.sin(self.theta)
        ce, se = np.cos(self.phi), np.sin(self.phi)
        cam = np.array([ce * ct, ce * st, se])               # unit vector origin -> camera (elev. phi)
        fwd = -cam                                           # viewing direction (into the screen)
        world_up = np.array([0.0, 0.0, 1.0])                 # +z is UP
        right = np.cross(fwd, world_up)
        n = np.linalg.norm(right)
        right = right / n if n > 1e-9 else np.array([1.0, 0.0, 0.0])   # looking straight down z
        up = np.cross(right, fwd)                            # exact screen-up (component of +z stays up)
        up = up / np.linalg.norm(up)
        self._R = np.array([right, up, cam])                 # rows: world -> (screen_x, screen_y, depth)
        return self

    def _view(self, point):
        p = np.asarray(point, dtype=float)
        return self._R @ p if self.mode == "3d" else p      # world -> camera frame

    def view_array(self, points):
        """Batched _view: (N,3) world points -> (N,3) camera-frame coords in one matmul."""
        pts = np.asarray(points, dtype=float).reshape(-1, 3)
        return pts @ self._R.T if self.mode == "3d" else pts

    def project(self, point):
        """3D world point -> (px, py)."""
        p = self._view(point)
        upp = self._upp
        px = self.pixel_width / 2 + p[0] / upp
        py = self.pixel_height / 2 - p[1] / upp   # pixel y grows downward
        return px, py

    def project_array(self, points):
        """Batched project: (N,3) world points -> (N,2) pixel coords in one matmul."""
        p = self.view_array(points)
        upp = self._upp
        px = self.pixel_width / 2 + p[:, 0] / upp
        py = self.pixel_height / 2 - p[:, 1] / upp
        return np.column_stack([px, py])

    def depth(self, point):
        """Signed depth along the view axis (+ = towards the viewer). Larger = drawn on top."""
        return float(self._view(point)[2])

    def unproject(self, px, py):
        """(px, py) -> world point. Inverse of project in 2D (used for click-picking); in 3D the
        in-plane inverse (depth assumed 0), good enough for picking flat objects."""
        h = (px - self.pixel_width / 2) * self._upp
        v = (self.pixel_height / 2 - py) * self._upp
        if self.mode == "3d":
            return self._R.T @ np.array([h, v, 0.0])         # un-rotate the in-plane point
        return h * RIGHT + v * UP
