from maze.consts import LEARNING_RATE, GAMMA, N_ROWS, N_COLS
import numpy as np

class QTable:

    def __init__(self):
        self.q_val = np.zeros((N_ROWS*N_COLS, 4))
    
    def state(self, row, col):
        return N_COLS * row + col

    def best_action(self, state):
        return self.q_val[state].argmax()
    
    def update(self, state, action, reward, next_state):
        self.q_val[state][action] += LEARNING_RATE * (reward + GAMMA * self.q_val[next_state].max())