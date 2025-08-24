from maze.app.consts import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH, FPS
import maze.app.visualizer as visual
import maze.generation.dfs as dfs
import maze.app.modes as modes
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
maze = dfs.create()

while running:
    # Handle user input
    for event in pygame.event.get():
        # User pressed X button
        if event.type == pygame.QUIT:
            running = False
            break
        
        # User pressed a key
        elif event.type == pygame.KEYDOWN:
            try:
                # Show the maze
                if event.key == pygame.K_0:
                    modes.showMaze(screen, clock, maze)

                # Generate the maze
                elif event.key == pygame.K_1:
                    maze = modes.generateMaze(screen, clock)

                # Solve the maze
                elif event.key == pygame.K_2:
                    modes.solveMaze(screen, clock, maze)
            
            # Close application
            except modes.QuitFromAppException:
                running = False

    # Draw GUI
    visual.drawMenu(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()