
# MAZE SIZE
N_ROWS, N_COLS = 15, 15
TILE_SIZE = 45

# Cell states
FREE_CELL = 1.
CHEESE = 0.75
MOUSE = 0.5
WALL = 0.

# Movements
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Image paths
MAZE_IMG_PATH = './assets/image/maze.png'
CHEESE_IMG_PATH = './assets/image/cheese.png'
MOUSE_IMG_PATH = './assets/image/mouse.png'
UP_ARROW_IMG = './assets/image/up-arrow.png'
DOWN_ARROW_IMG = './assets/image/down-arrow.png'
LEFT_ARROW_IMG = './assets/image/left-arrow.png'
RIGHT_ARROW_IMG = './assets/image/right-arrow.png'

INF = 1_000_000_000
FPS = 10