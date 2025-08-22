from maze.visualizer import drawPath, drawMaze
from maze.consts import N_ROWS, N_COLS, UP, DOWN, LEFT, RIGHT, FREE_CELL, MOUSE, WALL, CRASH_PENALTY, CHEESE, WIN_PRIZE, MOVE_COST, GO_BACK_PENALTY
import numpy as np
import torch

class QMaze:

    def __init__(self, maze):
        self.maze = maze
        self.path = None 
        self.mouse_pos = (1, 1)
        self.is_terminated = False
        self.vis = np.full((N_ROWS, N_COLS), False) 
    
    def reset(self):
        # Remove old mouse
        row, col = self.mouse_pos
        self.maze[row][col] = FREE_CELL

        # Spawn new mouse
        self.maze[1][1] = MOUSE
        self.mouse_pos = (1, 1)
        self.path = None
        self.is_terminated = False 
        self.vis = np.full((N_ROWS, N_COLS), False) 

    def is_terminated(self):
        return self.is_terminated

    def draw(self, screen):
        #drawPath(screen, self.maze, self.path)
        drawMaze(screen, self.maze)
        
    def toState(self):
        row, col = self.mouse_pos
        return N_COLS*row + col

    def updateMousePosition(self, row, col):
        # Remove old mouse
        old_row, old_col = self.mouse_pos
        self.maze[old_row][old_col] = FREE_CELL
        
        # Spawn new mouse
        self.mouse_pos = (row, col)
        self.maze[row][col] = MOUSE

    def act(self, action):
        r_change, c_change = 0, 0

        if action == UP:
            r_change = -1

        elif action == DOWN:
            r_change = 1

        elif action == LEFT:
            c_change = -1

        elif action == RIGHT:
            c_change = 1

        # Fetch mouse position
        old_state = self.toState()
        row, col = self.mouse_pos
        
        # Crashed into wall
        if self.maze[row+r_change][col+c_change] == WALL:
            self.is_terminated = True
            reward = CRASH_PENALTY
            
        # Found cheese
        elif self.maze[row+r_change][col+c_change] == CHEESE:
            self.is_terminated = True
            reward = WIN_PRIZE
            self.updateMousePosition(row+r_change, col+c_change)
            self.vis[row+r_change][col+c_change] = True
            
        # Safely moved
        elif self.maze[row+r_change][col+c_change] == FREE_CELL:
            self.is_terminated = False
            reward = MOVE_COST
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