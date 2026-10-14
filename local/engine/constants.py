import os
import numpy as np
# Coordinate convention (standard 2D view):
#   X positive to the right
#   Y positive up                                    (screen vertical)
#   Z positive towards the viewer / out of the screen  -> depth, ignored in 2D
#  0.0, 0.0, 0.0

ORIGIN = np.array([0.0, 0.0, 0.0])

RIGHT   = np.array([1.0, 0.0, 0.0])
LEFT    = np.array([-1.0, 0.0, 0.0])
UP      = np.array([0.0, 1.0, 0.0])
DOWN    = np.array([0.0, -1.0, 0.0])
TOWARDS = np.array([0.0, 0.0, 1.0])   # out of the screen, towards the viewer
AWAY    = np.array([0.0, 0.0, -1.0])  # into the screen

PIXEL_HEIGHT = 1080
PIXEL_WIDTH = 1920
FPS = 60

# Colors (RGB in 0..1)
WHITE  = (1.0, 1.0, 1.0)
BLACK  = (0.0, 0.0, 0.0)
GREY   = (0.53, 0.53, 0.53)
RED    = (0.89, 0.29, 0.20)
GREEN  = (0.51, 0.76, 0.42)
BLUE   = (0.35, 0.60, 0.92)
YELLOW = (1.0, 0.86, 0.35)

FRAME_HEIGHT = 8.0                       # how many world units fit vertically on screen
# -> units per pixel = FRAME_HEIGHT / PIXEL_HEIGHT  (used to map world coords to pixels)

# Output folders (absolute, relative to the project root = the parent of the engine/ package),
# so output lands in the right place no matter where the script is started from.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(_PROJECT_ROOT, "output_images")
VIDEO_DIR = os.path.join(_PROJECT_ROOT, "output_videos")
