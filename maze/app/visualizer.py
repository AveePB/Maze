"""
Maze visualizer.

This module contains basic visualization methods.

Author: Michał Zientek
Date: 2025-08-09
"""
from maze.app.consts import CHEESE, MOUSE, WALL, N_ROWS, N_COLS, TILE_SIZE, CHEESE_IMG_PATH, MOUSE_IMG_PATH, UP, DOWN, LEFT, RIGHT, UP_ARROW_IMG, DOWN_ARROW_IMG, LEFT_ARROW_IMG, RIGHT_ARROW_IMG
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

def drawMenu(screen: pygame.Surface):
    # Draw background
    bg_color = pygame.Color(204, 14, 0) # Red
    screen.fill(bg_color)

    # Draw logo
    logo = pygame.image.load('./assets/image/maze.png')
    logo = pygame.transform.scale(logo, (TILE_SIZE*6, TILE_SIZE*6))
    screen.blit(logo, ((N_COLS*TILE_SIZE - logo.get_width())//2, 50))

    # Draw header
    big_font = pygame.font.Font('./assets/font/main-font.ttf', size=20)
    header = big_font.render('Maze Menu', True, 'white')
    screen.blit(header, ((N_COLS*TILE_SIZE - header.get_width())//2, 360))

    # Draw first option
    mid_font = pygame.font.Font('./assets/font/main-font.ttf', size=15)
    show_label = mid_font.render('Show the maze (Press 0)', True, 'white')
    screen.blit(show_label, ((N_COLS*TILE_SIZE - show_label.get_width())//2, 410))

    # Draw second option
    generate_label = mid_font.render('Generate the maze (Press 1)', True, 'white')
    screen.blit(generate_label, ((N_COLS*TILE_SIZE - generate_label.get_width())//2, 460))

    # Draw third option
    solve_label = mid_font.render('Solve the maze (Press 2)', True, 'white')
    screen.blit(solve_label, ((N_COLS*TILE_SIZE - solve_label.get_width())//2, 510))

    # Draw watermark
    watermark = pygame.image.load('./assets/image/watermark.png')
    watermark = pygame.transform.scale(watermark, (TILE_SIZE,  TILE_SIZE))
    screen.blit(watermark, (N_COLS*TILE_SIZE - watermark.get_width(), N_ROWS*TILE_SIZE - watermark.get_height()))