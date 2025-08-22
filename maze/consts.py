"""
Maze constants.

This module contains essential constants that are use for the application.

Author: Michał Zientek
Date: 2025-08-10
"""
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

# Other parameters
INF = 1_000_000_000
FPS = 100

# Training parameters
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
DECAY_RATE = 0.001
MIN_EPSILON = 0.15
LEARNING_RATE = 0.001
GAMMA = 0.6

# Rewards
CRASH_PENALTY = -0.75
GO_BACK_PENALTY = -0.5
MOVE_COST = -0.04
WIN_PRIZE = 1.0
