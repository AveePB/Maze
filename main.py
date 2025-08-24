from maze.app.consts import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH
import maze.generation.kruskal as kruskal
import maze.generation.prim as prim
import maze.generation.dfs as dfs
import maze.solution.dijkstra as dijkstra
import maze.solution.qlearning as qlearning
import maze.solution.astar as astar
import pygame 
import numpy as np
import random

from collections import deque

# Initialize screen
screen = pygame.display.set_mode((N_COLS * TILE_SIZE, N_ROWS * TILE_SIZE))
pygame.display.set_icon(pygame.image.load(MAZE_IMG_PATH))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

maze = kruskal.create(screen, clock)
dijkstra.solve(maze, screen, clock)
qlearning.solve(maze, screen, clock)
astar.solve(maze, screen, clock)


pygame.quit()