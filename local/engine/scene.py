import os
from .AnimObject import AnimObject
from .camera import Camera
from .constants import FPS, IMAGE_DIR, VIDEO_DIR
# NOTE: renderScene (Cairo) and VideoWriter (ffmpeg) are imported LAZILY inside render()/
# render_video(), so the engine core imports cleanly in the browser (Pyodide), where only
# the Canvas backend is used and Cairo/ffmpeg are unavailable.


class Scene:
    def __init__(self):
        self.objectList: list[AnimObject] = []   # the objects to be drawn, in draw order
        self._writer = None                      # active VideoWriter during render_video()
        self.camera = Camera()                   # projection 3D->2D (swap for a 3D camera later)

    def add(self, *objects):
        self.objectList.extend(objects)          # accept one or several objects at once
        return self                              # allows chaining: scene.add(a).add(b)

    def construct(self):
        """Override in a subclass. Use self.add(...) for static objects, and
        self.play(...) / self.wait(...) for animation (when rendering a video)."""
        pass

    def _output_path(self, folder, extension, filename):
        """Where to save. Default: <folder>/<SceneClassName>.<ext>. A bare filename is placed
        in <folder>; a filename with a path (or absolute) is used as given."""
        if filename is None:
            filename = f"{type(self).__name__}.{extension}"
        if not os.path.isabs(filename) and os.path.dirname(filename) == "":
            os.makedirs(folder, exist_ok=True)
            return os.path.join(folder, filename)
        return filename

    # ---------- static image ----------
    def render(self, filename=None):
        """Build the scene via construct() and save a single image to output_images/."""
        from .renderScene import renderScene            # lazy: Cairo only needed locally
        self.construct()
        path = self._output_path(IMAGE_DIR, "png", filename)
        return renderScene(self, path)

    # ---------- animation / video ----------
    def render_video(self, filename=None):
        """Build the scene via construct() (which calls play()/wait()) and save an mp4 to output_videos/."""
        from .video import VideoWriter                  # lazy: ffmpeg only needed locally
        path = self._output_path(VIDEO_DIR, "mp4", filename)
        self._writer = VideoWriter(path)
        self.construct()
        self._writer.close()
        self._writer = None
        return path

    def play(self, *animations, run_time=1.0):
        """Run the given animations together over run_time seconds, writing one frame each tick."""
        for anim in animations:
            if anim.target not in self.objectList:
                self.objectList.append(anim.target)   # auto-add targets (e.g. FadeIn of a new object)
            anim.begin()
        if self._writer is None:                      # static image mode: jump straight to the end
            for anim in animations:
                anim.update(1.0)
            return
        total = max(1, round(run_time * FPS))
        for frame in range(total + 1):
            alpha = frame / total
            for anim in animations:
                anim.update(alpha)
            self._writer.write_frame(self.objectList, self.camera)

    def wait(self, duration=1.0):
        """Hold the current picture for 'duration' seconds (static frames)."""
        if self._writer is None:                      # static image mode: nothing to hold
            return
        for _ in range(max(1, round(duration * FPS))):
            self._writer.write_frame(self.objectList, self.camera)
