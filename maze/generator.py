import numpy as np
import random

WALL = 0.
UNVISITED = 3.
VISITED = 1.
MOUSE = .5

class Move:
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3

class MazeGenerator:
    
    def __init__(self, n_rows, n_cols):
        # Set settings
        self.n_rows = n_rows
        self.n_cols = n_cols

    def getMaze(self):
        # Create maze
        maze = np.full((2*self.n_rows - 1, 2*self.n_cols - 1), UNVISITED, dtype=float)
       
       # Build walls
        for row in range(1, 2*self.n_rows-1, 2): maze[row, :] = WALL
        for col in range(1, 2*self.n_cols-1, 2): maze[:, col] = WALL

        # Choose start position
        start_row = 2*random.randint(0, self.n_rows-1)
        start_col = 2*random.randint(0, self.n_cols-1)

        # Create paths
        self.__dfs(maze, start_row, start_col)
        maze[0][0] = MOUSE
        return maze
    
    def __dfs(self, maze, row, col):
        # Mark cell
        maze[row][col] = VISITED

        # Visit neighbours
        moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        random.shuffle(moves)

        for move in moves:
            # Go Upwards
            if move == Move.UP:
                # Cannot expand
                if row - 2 < 0 or maze[row - 2][col] == VISITED:
                    continue
                
                # Go to next cell
                maze[row - 1][col] = VISITED
                self.__dfs(maze, row-2, col)

            # Go Downwards
            elif move == Move.DOWN:
                # Cannot expand
                if row + 2 >= 2*self.n_rows-1 or maze[row + 2][col] == VISITED:
                    continue

                # Go to next cell
                maze[row + 1][col] = VISITED
                self.__dfs(maze, row+2, col)

            # Go Leftwards
            elif move == Move.LEFT:
                # Cannot expand
                if col - 2 < 0 or maze[row][col - 2] == VISITED:
                    continue

                # Go to next cell
                maze[row][col - 1] = VISITED
                self.__dfs(maze, row, col-2)
            
            # Go Rightwards
            else:
                # Cannot expand
                if col + 2 >= 2*self.n_cols-1 or maze[row][col + 2] == VISITED:
                    continue

                # Go to next cell
                maze[row][col + 1] = VISITED
                self.__dfs(maze, row, col+2)