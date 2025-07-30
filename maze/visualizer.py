from maze.generator import MOUSE, WALL
import pygame

MAZE_IMG_PATH = './assets/image/maze.png'
CHEESE_IMG_PATH = './assets/image/cheese.png'
MOUSE_IMG_PATH = './assets/image/mouse.png'

N_ROWS = 10
N_COLS = 10
TILE_SIZE = 32

def drawMaze(screen, maze, visited_cells):
    # Draw grid
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            # Create tile
            rect = (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Select color
            if maze[row][col] == MOUSE:
                color = pygame.Color(102, 102, 100) # Gray
            elif maze[row][col] == WALL:
                color = pygame.Color(204, 14, 0) # Red
            else:
                color = pygame.Color(252, 252, 252) # White
            
            # Draw cell
            pygame.draw.rect(screen, color, rect)
            if maze[row][col] == MOUSE: 
                texture = pygame.image.load(MOUSE_IMG_PATH)
                texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
                screen.blit(texture, rect)
    
    # Draw visited cells
    color = pygame.Color(42, 201, 10) # Lime

    # Draw cheese
    color = pygame.Color(252, 215, 3) # Yellow
    x = (len(maze[0]) - 1) * TILE_SIZE
    y = (len(maze) - 1) * TILE_SIZE
    rect = (x, y, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, color, rect)

    texture = pygame.image.load(CHEESE_IMG_PATH)
    texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
    screen.blit(texture, rect)
