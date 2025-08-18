from maze.consts import CHEESE, MOUSE, WALL, N_ROWS, N_COLS, TILE_SIZE, CHEESE_IMG_PATH, MOUSE_IMG_PATH, UP, DOWN, LEFT, RIGHT, UP_ARROW_IMG, DOWN_ARROW_IMG, LEFT_ARROW_IMG, RIGHT_ARROW_IMG
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

def drawPath(screen, maze, dist):
    drawMaze(screen, maze)

    # Draw grid
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # Create tile
            rect = (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Select color
            if dist[row][col] == UP:
                texture = pygame.image.load(UP_ARROW_IMG)
            elif dist[row][col] == DOWN:
                texture = pygame.image.load(DOWN_ARROW_IMG)
            elif dist[row][col] == LEFT:
                texture = pygame.image.load(LEFT_ARROW_IMG)
            elif dist[row][col] == RIGHT:
                texture = pygame.image.load(RIGHT_ARROW_IMG)
            else:
                continue
            texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
            screen.blit(texture, rect)