"""
Maze generator using randomized Kruskal's algorithm.

This module creates a random maze using an iterative approach of randomized Kruskal's algorithm. 
It can optionally display the maze generation step-by-step using pygame.

Author: Michał Zientek
Date: 2025-08-16
"""
from maze.consts import N_ROWS, N_COLS, FREE_CELL, CHEESE, MOUSE, WALL, KRUSKAL_FPS 
from maze.visualizer import drawMaze
from collections import deque
import numpy as np
import random
import pygame

def create(screen=None, clock=None):
    """
    Create a random maze using randomized kruskal's algorithm.
    
    Optionally display the maze on a pygame screen.
    
    Args:
        screen (pygame.Surface, optional): Screen to draw maze on. Defaults to None.
        clock (pygame.time.Clock, optional): Clock controls the frame rate. Defaults to None.
    
    Returns:
        np.ndarray: 2D array representing the maze.
    """
    # Initialize maze
    maze = np.full((N_ROWS, N_COLS), WALL, dtype=np.float32)
    union_find = UnionFind((N_ROWS//2)*(N_COLS//2))
    wall_list = deque()

    # Create chess board pattern
    for row in range(N_ROWS):
        for col in range(N_COLS):
            if row % 2 and col % 2:
                maze[row][col] = FREE_CELL
    
    # Identify walls between free cells
    for row in range(1, N_ROWS-1):
        for col in range(1, N_COLS-1):
            # Vertical wall
            if maze[row-1][col] == FREE_CELL and maze[row+1][col] == FREE_CELL:
                wall_list.append((row, col, False))
            
            # Horizontal wall
            elif maze[row][col-1] == FREE_CELL and maze[row][col+1] == FREE_CELL:
                wall_list.append((row, col, True))

    # Place mouse and cheese
    maze[1][1] = MOUSE
    maze[N_ROWS-2][N_COLS-2] = CHEESE

    # Display maze if screen is given
    if screen:
        for event in pygame.event.get():
            # Close window
            if event.type == pygame.QUIT:
                return
        drawMaze(screen, maze)
        pygame.display.flip()
        clock.tick(KRUSKAL_FPS)
    
    # Shuffle walls and start maze generation
    random.shuffle(wall_list)
    while union_find.count() > 1:
        row, col, is_horizontal = wall_list.pop()

        # Vertical wall removal
        if not is_horizontal and union_find.find(union_find.cell_id(row-1, col)) != union_find.find(union_find.cell_id(row+1, col)):
            union_find.union(union_find.cell_id(row-1, col), union_find.cell_id(row+1, col))
            maze[row][col] = FREE_CELL

        # Horizontal wall removal
        elif is_horizontal and union_find.find(union_find.cell_id(row, col-1)) != union_find.find(union_find.cell_id(row, col+1)):
            union_find.union(union_find.cell_id(row, col-1), union_find.cell_id(row, col+1))
            maze[row][col] = FREE_CELL
        
        # Update display
        if screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            drawMaze(screen, maze)
            pygame.display.flip()
            clock.tick(KRUSKAL_FPS)
    
    return maze


class UnionFind:
    """
    Simple Union-Find (Disjoint Set) class for maze generation.
    """

    def __init__(self, size):
        """
        Create Union-Find with given number of elements.
        
        Args:
            size (int): Number of elements.
        """
        self.parents = np.arange(size)
        self.size = size

    def find(self, x):
        """
        Find root parent of element x with path compression.
        
        Args:
            x (int): Element index.
        
        Returns:
            int: Root parent index.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        """
        Join sets containing x and y.
        
        Args:
            x (int): First element index.
            y (int): Second element index.
        """
        self.parents[self.find(x)] = self.find(y)
    
    def count(self):
        """
        Count number of separate sets.
        
        Returns:
            int: Number of sets.
        """
        n_unions = 0
        for i in range(self.size):
            if self.parents[i] == i:
                n_unions += 1
        return n_unions
    
    def cell_id(self, row, col):
        """
        Convert maze cell coordinates to Union-Find index.
        
        Args:
            row (int): Row index in maze.
            col (int): Column index in maze.
        
        Returns:
            int: Index in Union-Find structure.
        """
        return (row//2)*(N_COLS//2) + (col//2)
