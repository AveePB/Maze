from maze.app.consts import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH, FPS
import maze.app.visualizer as visual
import pygame 
import time

# Initialize screen
screen = pygame.display.set_mode((N_COLS * TILE_SIZE, N_ROWS * TILE_SIZE))
pygame.display.set_icon(pygame.image.load(MAZE_IMG_PATH))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()
pygame.init()

# Game parameters
running = True
maze = None

while running:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
        elif event.type == pygame.KEYDOWN:
            # Show the maze
            if event.key == pygame.K_0:
                ...

            # Generate the maze
            elif event.key == pygame.K_1:
                ...

            # Solve the maze
            elif event.key == pygame.K_2:
                ...

    # Draw GUI
    visual.drawMenu(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()