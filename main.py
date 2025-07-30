from maze.generator import MazeGenerator
from maze.visualizer import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH, drawMaze
import pygame

# Constants
IS_TRAINING = True
FPS = 5

# Initialize screen
screen = pygame.display.set_mode(((2 * N_COLS - 1) * TILE_SIZE, (2 * N_ROWS - 1) * TILE_SIZE))
pygame.display.set_icon(pygame.image.load(MAZE_IMG_PATH))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

# Initialize game 
generator = MazeGenerator(N_ROWS, N_COLS)
visited_cells = []
is_running = True

while is_running:
    # Handle user input
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            is_running = False
            break

    # Fetch maze
    maze = generator.getMaze()
    
    # Draw game
    drawMaze(screen, maze, visited_cells)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    