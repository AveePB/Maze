from maze.consts import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH
import maze.generation.dfs as dfs
import maze.generation.kruskal as kruskal
import maze.generation.prim as prim
import maze.solution.dijkstra as dijkstra
import pygame

# Initialize screen
screen = pygame.display.set_mode((N_COLS * TILE_SIZE, N_ROWS * TILE_SIZE))
pygame.display.set_icon(pygame.image.load(MAZE_IMG_PATH))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

maze = prim.create()
path = dijkstra.solve(maze, screen)
print(path)

pygame.quit()
    