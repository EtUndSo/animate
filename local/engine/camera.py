import numpy as np
from .constants import PIXEL_WIDTH, PIXEL_HEIGHT, FRAME_HEIGHT, RIGHT, UP


class Camera:
    """Maps 3D world points to 2D pixel coordinates - the single place that knows about
    PROJECTION. This keeps the engine 3D-ready (like Manim): the default 2D camera projects
    orthographically onto RIGHT/UP and drops depth; a future 3D camera adds position,
    orientation and perspective HERE, and nothing else in the engine changes - points are
    already 3D (N,3) and the transforms (shift/scale/rotate) already work in 3D.
    """

    def __init__(self, pixel_width=PIXEL_WIDTH, pixel_height=PIXEL_HEIGHT, frame_height=FRAME_HEIGHT):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height
        self.units_per_pixel = frame_height / pixel_height

    def project(self, point):
        """3D world point -> (px, py). 2D orthographic: horizontal = point.RIGHT, vertical =
        point.UP; the depth axis is dropped. (A 3D camera would rotate/perspective-divide here.)"""
        point = np.asarray(point, dtype=float)
        h = np.dot(point, RIGHT)
        v = np.dot(point, UP)
        px = self.pixel_width / 2 + h / self.units_per_pixel
        py = self.pixel_height / 2 - v / self.units_per_pixel      # minus: pixel y grows downward
        return px, py
