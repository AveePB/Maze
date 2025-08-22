"""
Maze generator using Prim's algorithm.

This module generates a random maze using Prim's algorithm.
It can optionally display the maze generation step-by-step using pygame.

Author: Michał Zientek
Date: 2025-08-16
"""
from maze.app.consts import N_ROWS, N_COLS, FREE_CELL, CHEESE, MOUSE, WALL, PRIM_FPS 
from maze.app.visualizer import drawMaze
import numpy as np
import random
import pygame

def create(screen=None, clock=None):
    """
    Generate a maze using Prim's algorithm.

    Starts with a random cell, marks it as free,
    and then grows the maze by expanding walls
    until all cells are connected.

    Args:
        screen (pygame.Surface, optional): If given, the maze is displayed step by step.
        clock (pygame.time.Clock, optional): Clock controls the frame rate. Defaults to None.
    
    Returns:
        np.ndarray: 2D numpy array with the final maze.
    """
    # Initialize maze
    maze = np.full((N_ROWS, N_COLS), WALL, dtype=np.float32)
    wall_list = []

    # Choose start position
    row = 2*random.randint(0, N_ROWS // 2 - 1) + 1
    col = 2*random.randint(0, N_COLS // 2 - 1) + 1
    maze[row][col] = FREE_CELL
    
    
    __expandMaze(wall_list, row, col)

    # Display maze
    if screen:
        # Handle user input
        for event in pygame.event.get():
            # Close window
            if event.type == pygame.QUIT:
                return
            
        drawMaze(screen, maze)
        pygame.display.flip()
        clock.tick(PRIM_FPS)

    # Visit all cells seperated by walls
    random.shuffle(wall_list)
    while len(wall_list):
        # Pop wall
        wall, cell = random.choice(wall_list)
        wall_list.remove((wall, cell))

        # Unpack data
        w_row, w_col = wall
        c_row, c_col = cell

        # Cell is unvisited
        if maze[c_row][c_col] == WALL or maze[row][col] == MOUSE or maze[row][col] == CHEESE:
            maze[w_row][w_col] = FREE_CELL
            maze[c_row][c_col] = FREE_CELL
            __expandMaze(wall_list, c_row, c_col)

        # Display maze
        if screen:
            # Handle user input
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    return
                
            drawMaze(screen, maze)
            pygame.display.flip()
            clock.tick(PRIM_FPS)
    
    # Place mouse and cheese
    maze[1][1] = MOUSE
    maze[N_ROWS-2][N_COLS-2] = CHEESE

    # Display maze
    if screen:
        # Handle user input
        for event in pygame.event.get():
            # Close window
            if event.type == pygame.QUIT:
                return
                
        drawMaze(screen, maze)
        pygame.display.flip()
        clock.tick(PRIM_FPS)

    return maze

def __expandMaze(wall_list, row, col):
    """
    Add walls and their opposite cells to the wall list.

    Args:
        wall_list (list): List of walls with their neighbor cells.
        row (int): Current cell row.
        col (int): Current cell column.
    """
    # Add top wall + cell
    if row-2 > 0:
        wall_list.append(((row-1, col), (row-2, col)))
    
    # Add bottom wall + cell
    if row+2 < N_ROWS:
        wall_list.append(((row+1, col), (row+2, col)))
    
    # Add left wall + cell
    if col-2 > 0:
        wall_list.append(((row, col-1), (row, col-2)))
    
    # Add right wall + cell
    if col+2 < N_COLS:
        wall_list.append(((row, col+1), (row, col+2)))