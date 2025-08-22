"""
Maze solver using Q-Learning.

This module solves a maze using a Q-tables.
It can optionally display the maze solution step-by-step using pygame.

Author: Michał Zientek
Date: 2025-08-22
"""
from maze.app.consts import LEARNING_RATE, GAMMA, N_ROWS, N_COLS, MIN_EPSILON, DECAY_RATE, CRASH_PENALTY, WIN_PRIZE, UP, DOWN, LEFT, RIGHT, FPS, QLEARNING_FPS
from maze.app.visualizer import drawPath
from collections import deque
import maze.solution.env as env
import numpy as np
import random
import pygame

class QTable:
    """
    Q-Table implementation for tabular Q-learning.

    Attributes:
        q_val (np.ndarray): 2D array storing Q-values for each state-action pair.
                            Shape: (N_ROWS * N_COLS, 4), where 4 = number of actions.
    """

    def __init__(self):
        """
        Initializes the Q-table with zeros.
        Each state corresponds to a maze cell (row, col) mapped to a single index.
        Each action corresponds to a movement (UP, DOWN, LEFT, RIGHT).
        """
        self.q_val = np.zeros((N_ROWS * N_COLS, 4))
    
    def state(self, row, col):
        """
        Converts a 2D maze coordinate (row, col) to a 1D state index.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            int: Flattened state index for Q-table lookup.
        """
        return N_COLS * row + col

    def best_action(self, state):
        """
        Returns the best action (with the highest Q-value) for a given state.

        Args:
            state (int): Flattened state index.

        Returns:
            int: Index of the optimal action (0=UP, 1=DOWN, 2=LEFT, 3=RIGHT).
        """
        return self.q_val[state].argmax()
    
    def update(self, state, action, reward, next_state):
        """
        Updates the Q-value for a given state-action pair using the Q-learning update rule:

            Q(s, a) = Q(s, a) + α * (reward + γ * max(Q(s', a')) - Q(s, a))

        Args:
            state (int): Current state index.
            action (int): Action taken at the current state.
            reward (float): Immediate reward received after taking the action.
            next_state (int): State index after taking the action.
        """
        self.q_val[state][action] += LEARNING_RATE * (
            reward + GAMMA * self.q_val[next_state].max()
        )

def solve(maze, screen=None, clock=None):
    """
    Solve a maze using Q-learning tables.

    Optionally display maze solution step on pygame screen.
    
    Args:
        maze (np.ndarray): 2D array representing the maze.
        screen (pygame.Surface, optional): Screen to draw maze. Defaults to None.
        clock (pygame.time.Clock, optional): Clock controls the frame rate. Defaults to None.

    Returns:
        np.ndarray: 2D array representing the path.        
    """
    # Initialize structures
    qmaze = env.QMaze(maze)
    qtable = QTable()
    path = np.full(maze.shape, None)

    # Initialize parameters
    total_reward = 0.0
    epsilon = 1.0
    running = True

    # Infinitive number of episodes
    while running:
        # Exploration    
        if random.random() < epsilon:
            action = random.randint(0, 3)
        
        # Exploitation
        else:
            action = qtable.best_action(qmaze.toState())
        epsilon = max(MIN_EPSILON, epsilon - DECAY_RATE)

        # Perform action    
        old_state, action, reward, next_state, terminated = qmaze.act(action)
        qtable.update(old_state, action, reward, next_state)
        total_reward += reward

        # Terminate current episode
        if terminated and total_reward < CRASH_PENALTY*N_ROWS*N_COLS:
            total_reward = 0.0
            qmaze.reset()

        # Won the game
        elif terminated and reward == WIN_PRIZE:
            running = False
        
        # Draw GUI
        if screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            qmaze.draw(screen)
            pygame.display.flip()
            clock.tick(QLEARNING_FPS)
    
    # Reset positions
    qmaze.updateMousePosition(1, 1)
    qmaze.respawnCheese()
    
    # Save path from start to end
    path = np.full(maze.shape, None)
    stck = deque()
    stck.append((1, 1))

    while len(stck):
        row, col = stck.pop()
        
        # Save movement
        if qmaze.path[row][col] == UP:
            stck.append((row-1, col))
            path[row][col] = UP
        
        elif qmaze.path[row][col] == DOWN:
            stck.append((row+1, col))
            path[row][col] = DOWN
        
        elif qmaze.path[row][col] == LEFT:
            stck.append((row, col-1))
            path[row][col] = LEFT
        
        elif qmaze.path[row][col] == RIGHT:
            stck.append((row, col+1))
            path[row][col] = RIGHT

        # Remove arrow from mouse cell
        if row == 1 and col == 1:
            path[1][1] = None

        # Visualize solution
        if screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            drawPath(screen, maze, path)
            pygame.display.flip()
            clock.tick(FPS)
    
    return path
    
