from maze.consts import CHEESE, MOUSE, WALL, N_ROWS, N_COLS, TILE_SIZE, CHEESE_IMG_PATH, MOUSE_IMG_PATH
import pygame

def drawMaze(screen, maze):
    # Draw grid
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # Create tile
            rect = (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Select color
            if maze[row][col] == CHEESE:
                color = pygame.Color(252, 215, 3) # Yellow
            elif maze[row][col] == MOUSE:
                color = pygame.Color(102, 102, 100) # Gray
            elif maze[row][col] == WALL:
                color = pygame.Color(204, 14, 0) # Red
                #color = pygame.Color(0, 0, 0) # Black
            else:
                color = pygame.Color(252, 252, 252) # White
            
            # Draw cell and texture
            pygame.draw.rect(screen, color, rect)
            if maze[row][col] == CHEESE: 
                texture = pygame.image.load(CHEESE_IMG_PATH)
                texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
                screen.blit(texture, rect)

            elif maze[row][col] == MOUSE: 
                texture = pygame.image.load(MOUSE_IMG_PATH)
                texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
                screen.blit(texture, rect)