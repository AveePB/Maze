from maze.consts import N_ROWS, N_COLS, TILE_SIZE, MAZE_IMG_PATH, MOUSE, UP, DOWN, LEFT, RIGHT, FREE_CELL, WALL, CHEESE, FPS, WIN_PRIZE, CRASH_PENALTY, DECAY_RATE, MIN_EPSILON
import maze.generation.dfs as dfs
import maze.generation.kruskal as kruskal
import maze.generation.prim as prim
import maze.solution.dijkstra as dijkstra
import maze.solution.env as env
from maze.solution.qlearning import QTable
import pygame 
import numpy as np
import random

# Initialize screen
screen = pygame.display.set_mode((N_COLS * TILE_SIZE, N_ROWS * TILE_SIZE))
pygame.display.set_icon(pygame.image.load(MAZE_IMG_PATH))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

# Initialize parameters
qmaze = env.QMaze(dfs.create())
qtable = QTable()
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
        print('You won congratulations')
        running = False
        
    # Draw GUI
    qmaze.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
    
