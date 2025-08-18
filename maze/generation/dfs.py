"""
Maze generator using depth-first search (DFS).

This module creates a random maze using a stack-based DFS algorithm.
It can optionally display the maze generation step-by-step using pygame.

Author: Michał Zientek
Date: 2025-08-15
"""
from maze.consts import N_ROWS, N_COLS, FREE_CELL, CHEESE, MOUSE, WALL, UP, DOWN, LEFT, RIGHT, FPS
from maze.visualizer import drawMaze
from collections import deque
import numpy as np
import random
import pygame

def create(screen=None, clock=None):
    """
    Create a random maze using depth-first search (DFS) with stack.
    
    Optionally display maze generation step on pygame screen.
    
    Args:
        screen (pygame.Surface, optional): Screen to draw maze. Defaults to None.
        clock (pygame.time.Clock, optional): Clock controls the frame rate. Defaults to None.
    
    Returns:
        np.ndarray: 2D array representing the maze.
    """
    # Initialize maze
    maze = np.full((N_ROWS, N_COLS), WALL, dtype=np.float32)
    vis = set()

    # Create chess board
    for row in range(N_ROWS):
        for col in range(N_COLS):
            if row % 2 and col % 2:
                maze[row][col] = FREE_CELL

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
        clock.tick(FPS)

    # Choose start position
    row = 2*random.randint(0, N_ROWS // 2 - 1) + 1
    col = 2*random.randint(0, N_COLS // 2 - 1) + 1

    stack = deque()
    stack.append((row, col))
    vis.add((row, col))

    # Analyze rest of cells
    while len(stack):
        # Mark cell as visited
        row, col = stack.pop()

        moves = [UP, DOWN, LEFT, RIGHT]
        random.shuffle(moves)
        
        # Check each move for
        for move in moves:
           # Go Upwards
            if move == UP:
                # Cannot expand
                if row - 2 < 0 or (row-2, col) in vis:
                    continue
                
                # Push onto stack
                maze[row - 1][col] = FREE_CELL
                vis.add((row-2, col))
                stack.append((row-2, col))

            # Go Downwards
            elif move == DOWN:
                # Cannot expand
                if row + 2 >= N_ROWS or (row+2, col) in vis:
                    continue

                # Go to next cell
                maze[row + 1][col] = FREE_CELL
                vis.add((row+2, col))
                stack.append((row+2, col))

            # Go Leftwards
            elif move == LEFT:
                # Cannot expand
                if col - 2 < 0 or (row, col-2) in vis:
                    continue

                # Go to next cell
                maze[row][col - 1] = FREE_CELL
                vis.add((row, col-2))
                stack.append((row, col-2))
            
            # Go Rightwards
            else:
                # Cannot expand
                if col + 2 >= N_COLS or (row, col+2) in vis:
                    continue

                # Go to next cell
                maze[row][col + 1] = FREE_CELL
                vis.add((row, col+2))
                stack.append((row, col+2))

        # Display maze
        if screen:
            # Handle user input
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    return
                
            drawMaze(screen, maze)
            pygame.display.flip()
            clock.tick(FPS)
    
    return maze