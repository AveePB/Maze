"""
Maze Q-learning version.

This module contains q-learning optimized maze structure.

Author: Michał Zientek
Date: 2025-08-22
"""
from maze.app.visualizer import drawMaze
from maze.app.consts import N_ROWS, N_COLS, UP, DOWN, LEFT, RIGHT, FREE_CELL, MOUSE, WALL, CRASH_PENALTY, CHEESE, WIN_PRIZE, MOVE_COST, GO_BACK_PENALTY
import numpy as np

class QMaze:
    """
    Environment wrapper for a Q-learning maze-solving agent.

    Attributes:
        maze (np.ndarray): 2D grid representing the maze layout.
        path (np.ndarray): Stores the direction taken at each cell (for visualization).
        mouse_pos (tuple): Current position of the mouse (row, col).
        is_terminated (bool): Indicates whether the episode has ended.
        vis (np.ndarray): Boolean grid marking visited cells.
    """

    def __init__(self, maze):
        """
        Initializes the QMaze environment.

        Args:
            maze (np.ndarray): 2D array representing the maze structure.
        """
        self.maze = maze
        self.path = np.full(maze.shape, None)
        self.mouse_pos = (1, 1)
        self.is_terminated = False
        self.vis = np.full((N_ROWS, N_COLS), False) 
    
    def reset(self):
        """
        Resets the maze to its initial state:
        - Removes old mouse position.
        - Places the mouse at the starting position (1,1).
        - Clears the visited path and marks all cells as unvisited.
        - Resets the termination flag.
        """
        # Remove old mouse
        row, col = self.mouse_pos
        self.maze[row][col] = FREE_CELL

        # Spawn new mouse
        self.maze[1][1] = MOUSE
        self.mouse_pos = (1, 1)
        self.path = np.full(self.maze.shape, None)
        self.is_terminated = False 
        self.vis = np.full((N_ROWS, N_COLS), False) 

    def is_terminated(self):
        """
        Checks whether the current episode is finished.

        Returns:
            bool: True if the mouse has crashed or reached the cheese, False otherwise.
        """
        return self.is_terminated

    def draw(self, screen):
        """
        Draws the current maze state to the Pygame screen.

        Args:
            screen (pygame.Surface): Pygame surface where the maze is drawn.
        """
        drawMaze(screen, self.maze)
        
    def toState(self):
        """
        Converts the current mouse position (row, col) to a unique state index.

        Returns:
            int: Flattened state index used by Q-learning.
        """
        row, col = self.mouse_pos
        return N_COLS*row + col

    def updateMousePosition(self, row, col):
        """
        Updates the mouse position on the maze grid.

        Args:
            row (int): New row position of the mouse.
            col (int): New column position of the mouse.
        """
        # Remove old mouse
        old_row, old_col = self.mouse_pos
        self.maze[old_row][old_col] = FREE_CELL
        
        # Spawn new mouse
        self.mouse_pos = (row, col)
        self.maze[row][col] = MOUSE
    
    def respawnCheese(self):
        """
        Places the cheese at the goal position (bottom-right corner).
        """
        self.maze[N_ROWS-2][N_COLS-2] = CHEESE
        
    def act(self, action):
        """
        Executes the given action in the maze environment.

        The mouse attempts to move in the chosen direction:
        - If it hits a wall, the episode ends with a crash penalty.
        - If it reaches the cheese, the episode ends with a reward.
        - If it moves to a free cell, it receives a small reward or penalty if revisiting.

        Args:
            action (int): The action to perform (UP, DOWN, LEFT, RIGHT).

        Returns:
            tuple: (old_state, action, reward, new_state, terminated)
                - old_state (int): Previous state index.
                - action (int): Action taken.
                - reward (float): Reward obtained after the action.
                - new_state (int): New state index after the action.
                - terminated (bool): Whether the episode has ended.
        """
        r_change, c_change = 0, 0
        
        # Fetch mouse position
        old_state = self.toState()
        row, col = self.mouse_pos
        
        if action == UP:
            r_change = -1
            self.path[row][col] = UP

        elif action == DOWN:
            r_change = 1
            self.path[row][col] = DOWN

        elif action == LEFT:
            c_change = -1
            self.path[row][col] = LEFT

        elif action == RIGHT:
            c_change = 1
            self.path[row][col] = RIGHT
        
        # Crashed into wall
        if self.maze[row+r_change][col+c_change] == WALL:
            self.is_terminated = True
            reward = CRASH_PENALTY
            self.path[row][col] = None
            
        # Found cheese
        elif self.maze[row+r_change][col+c_change] == CHEESE:
            self.is_terminated = True
            reward = WIN_PRIZE
            self.updateMousePosition(row+r_change, col+c_change)
            self.vis[row+r_change][col+c_change] = True
            
        # Safely moved
        elif self.maze[row+r_change][col+c_change] == FREE_CELL:
            self.is_terminated = False
            self.updateMousePosition(row+r_change, col+c_change)

            # Unproductive movement
            if self.vis[row+r_change][col+c_change]:
                reward = GO_BACK_PENALTY
            
            # Right movement
            else:
                reward = MOVE_COST
                self.vis[row+r_change][col+c_change] = True

        new_state = self.toState()

        return old_state, action, reward, new_state, self.is_terminated
