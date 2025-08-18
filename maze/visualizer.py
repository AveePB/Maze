"""
Maze visualizer.

This module contains basic visualization methods.

Author: Michał Zientek
Date: 2025-08-09
"""
from maze.consts import CHEESE, MOUSE, WALL, N_ROWS, N_COLS, TILE_SIZE, CHEESE_IMG_PATH, MOUSE_IMG_PATH, UP, DOWN, LEFT, RIGHT, UP_ARROW_IMG, DOWN_ARROW_IMG, LEFT_ARROW_IMG, RIGHT_ARROW_IMG
import pygame

def drawMaze(screen, maze):
    """
    Draw the maze grid on the given Pygame screen.

    Each cell is rendered as a colored tile:
    - Cheese cells are yellow with a cheese texture.
    - Mouse cells are gray with a mouse texture.
    - Wall cells are red.
    - Empty cells are white.

    Args:
        screen (pygame.Surface): Pygame surface to draw on.
        maze (np.ndarray): 2D array representing the maze.
    """
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

def drawPath(screen, maze, path):
    """
    Draw the maze with arrows indicating the solution path.

    First draws the maze with `drawMaze()`, then overlays arrow textures
    on cells that belong to the solution path:
    - UP, DOWN, LEFT, or RIGHT arrows are displayed.
    - Cells without directions are skipped.

    Args:
        screen (pygame.Surface): Pygame surface to draw on.
        maze (np.ndarray): 2D array representing the maze.
        path (np.ndarray): 2D array of directions (UP, DOWN, LEFT, RIGHT, or None).
    """
    drawMaze(screen, maze)

    # Draw grid
    for row in range(N_ROWS):
        for col in range(N_COLS):
            # Create tile
            rect = (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # Select color
            if path[row][col] == UP:
                texture = pygame.image.load(UP_ARROW_IMG)
            elif path[row][col] == DOWN:
                texture = pygame.image.load(DOWN_ARROW_IMG)
            elif path[row][col] == LEFT:
                texture = pygame.image.load(LEFT_ARROW_IMG)
            elif path[row][col] == RIGHT:
                texture = pygame.image.load(RIGHT_ARROW_IMG)
            else:
                continue
            texture = pygame.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
            screen.blit(texture, rect)