"""
Maze solver using dijkstra's algorithm.

This module solves a maze using a variant of dijkstra's algorithm.
It can optionally display the maze solution step-by-step using pygame.

Author: Michał Zientek
Date: 2025-08-18
"""
from maze.consts import UP, DOWN, LEFT, RIGHT, WALL, INF, N_ROWS, N_COLS, FPS
from maze.visualizer import drawPath
from collections import deque
import numpy as np
import pygame

def solve(maze, screen=None):
    """
    Solve a maze using dijkstra's algorithm with stack.

    Optionally display maze solution step on pygame screen.
    
    Args:
        maze (np.ndarray): 2D array representing the maze.
        screen (pygame.Surface, optional): Screen to draw maze. Defaults to None.

    Returns:
        np.ndarray: 2D array representing the path.        
    """
    # Create required structures
    dist = np.full((*maze.shape,2), (None, INF))
    vis = maze == WALL
    stck = deque()

    # Pick target node
    dist[N_ROWS-2][N_COLS-2] = (None, 0)
    stck.append((N_ROWS-2, N_COLS-2))

    while len(stck):
        row, col = stck.pop()

        # Node already processed
        if vis[row][col]: continue
        
        # Update nearby cells
        if not vis[row-1][col] and dist[row-1][col][1] > dist[row][col][1] + 1: # Up cell
            dist[row-1][col] = (DOWN, dist[row][col][1] + 1)
            stck.append((row-1, col))
        
        if not vis[row+1][col] and dist[row+1][col][1] > dist[row][col][1] + 1: # Down cell
            dist[row+1][col] = (UP, dist[row][col][1] + 1)
            stck.append((row+1, col))

        if not vis[row][col-1] and dist[row][col-1][1] > dist[row][col][1] + 1: # Left cell
            dist[row][col-1] = (RIGHT, dist[row][col][1] + 1)
            stck.append((row, col-1))

        if not vis[row][col+1] and dist[row][col+1][1] > dist[row][col][1] + 1: # Right cell
            dist[row][col+1] = (LEFT, dist[row][col][1] + 1)
            stck.append((row, col+1))

        # Mark as visited
        vis[row][col] = True
    
    # Save path from start to end
    path = np.full(maze.shape, None)
    stck.append((1, 1))

    while len(stck):
        row, col = stck.pop()
        
        # Save movement
        path[row][col] = dist[row][col][0]
        
        if path[row][col] == UP:
            stck.append((row-1, col))
        
        elif path[row][col] == DOWN:
            stck.append((row+1, col))
        
        elif path[row][col] == LEFT:
            stck.append((row, col-1))
        
        elif path[row][col] == RIGHT:
            stck.append((row, col+1))
        
        # Remove arrow from mouse cell
        if row == 1 and col == 1:
            path[1][1] = None

        # Visualize solution
        if screen:
            clock = pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            drawPath(screen, maze, path)
            pygame.display.flip()
            clock.tick(FPS)
    
    return path