import subprocess
import imageio_ffmpeg
from .constants import PIXEL_WIDTH, PIXEL_HEIGHT, FPS
from .renderScene import render_to_surface


class VideoWriter:
    """Streams rendered frames to ffmpeg (bundled via imageio-ffmpeg) and writes an mp4.

    Cairo's ARGB32 surface is laid out as BGRA bytes in memory, so we tell ffmpeg -pix_fmt bgra.
    The output is yuv420p for broad player compatibility.
    """

    def __init__(self, filename):
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        self.proc = subprocess.Popen(
            [ffmpeg, "-y",
             "-f", "rawvideo", "-pix_fmt", "bgra",
             "-s", f"{PIXEL_WIDTH}x{PIXEL_HEIGHT}", "-r", str(FPS),
             "-i", "-",
             "-pix_fmt", "yuv420p", filename],
            stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    def write_frame(self, objectList, camera=None):
        surface = render_to_surface(objectList, camera)
        self.proc.stdin.write(bytes(surface.get_data()))

    def close(self):
        self.proc.stdin.close()
        self.proc.wait()
