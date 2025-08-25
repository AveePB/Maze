"""
Maze modes handler.

This module contains basic mode handler methods.

Author: Michał Zientek
Date: 2025-08-25
"""
from maze.app.consts import FPS, N_COLS, TILE_SIZE, N_ROWS
import maze.generation.dfs as dfs
import maze.generation.kruskal as kruskal
import maze.generation.prim as prim
import maze.solution.dijkstra as dijkstra
import maze.solution.astar as astar
import maze.solution.qlearning as qlearning

import maze.app.visualizer as visual
import pygame

class QuitFromAppException(Exception):
    """
    Custom exception to indicate that the user wants to quit the application.

    This is raised when the user clicks the window's close button (X).
    """
    
    def __init__(self, *args):
        super().__init__(*args)

def pause(screen, clock):
    # Draw go back message
    mid_font = pygame.font.Font('./assets/font/main-font.ttf', size=15)
    go_back_label = mid_font.render('Go back to menu (Press q)', True, 'white')
    screen.blit(go_back_label, ((N_COLS*TILE_SIZE - go_back_label.get_width())//2, N_ROWS*TILE_SIZE-2*go_back_label.get_height()))

    pygame.display.flip()
    clock.tick(FPS)
    running = True
    
    while running:
    # Handle user input
        for event in pygame.event.get():
            # User pressed X button
            if event.type == pygame.QUIT:
                raise QuitFromAppException()                
            
            # User pressed a key
            elif event.type == pygame.KEYDOWN:
                # Stop showing the maze
                if event.key == pygame.K_q:
                    running = False
                    break

def showMaze(screen, clock, maze):
    """
    Display the maze on the screen and handle user input.

    The function continuously renders the maze and listens for events until the user
    either presses the '0' key to return to the menu or closes the window.

    Args:
        screen (pygame.Surface): The Pygame surface to draw the maze on.
        clock (pygame.time.Clock): The Pygame clock used to control the frame rate.
        maze (list): The maze data structure, typically a 2D list representing maze tiles.

    Raises:
        QuitFromAppException: Raised if the user clicks the window's close button (X), indicating the app should quit.
    """

    # Show the maze
    visual.drawMaze(screen, maze)
    pause(screen, clock)


def generateMaze(screen, clock):
    """
    Display the maze generation menu and create a maze using the selected algorithm.

    This function shows a menu that allows the user to select a maze generation 
    algorithm (DFS, Kruskal, or Prim) and returns the generated maze. The user can 
    also quit the application or return to the main menu.

    Args:
        screen (pygame.Surface): The Pygame surface to draw the maze on.
        clock (pygame.time.Clock): The Pygame clock used to control the frame rate.
    
    Returns:
            The generated maze as a NumPy array if one of the algorithms completes 
            successfully. Returns None if the user quits without generating a maze.

    Raises:
        QuitFromAppException: Raised if the user clicks the window's close button (X), indicating the app should quit.
    """
    running = True

    while running:
        # Handle user input
        for event in pygame.event.get():
            # User pressed X button
            if event.type == pygame.QUIT:
                raise QuitFromAppException()                
            
            # User pressed a key
            elif event.type == pygame.KEYDOWN:
                # Stop showing the maze
                if event.key == pygame.K_q:
                    running = False
                
                # Use dfs
                elif event.key == pygame.K_0:
                    maze = dfs.create(screen, clock)
                    if maze is None:
                        raise QuitFromAppException()
                    pause(screen, clock)
                    return maze
                
                # Use kruksal
                elif event.key == pygame.K_1:
                    maze = kruskal.create(screen, clock)
                    if maze is None:
                        raise QuitFromAppException()
                    pause(screen, clock)
                    return maze
                
                # Use prim
                elif event.key == pygame.K_2:
                    maze = prim.create(screen, clock)
                    if maze is None:
                        raise QuitFromAppException()
                    pause(screen, clock)
                    return maze
                
        # Draw the menu
        visual.drawGenerationMenu(screen)

        # Draw go back message
        mid_font = pygame.font.Font('./assets/font/main-font.ttf', size=15)
        go_back_label = mid_font.render('Go back to menu (Press q)', True, 'white')
        screen.blit(go_back_label, ((N_COLS*TILE_SIZE - go_back_label.get_width())//2, N_ROWS*TILE_SIZE-2*go_back_label.get_height()))

        pygame.display.flip()
        clock.tick(FPS)

def solveMaze(screen, clock, maze):
    """
    Display the maze-solving menu and solve the given maze using a selected algorithm.

    This function presents a menu to the user, allowing them to choose a pathfinding 
    algorithm to solve the provided maze. It handles user input, executes the chosen 
    algorithm, and pauses after completion.

    Args:
        screen (pygame.Surface): The Pygame surface to draw the maze on.
        clock (pygame.time.Clock): The Pygame clock used to control the frame rate.
        maze (list): The maze data structure, typically a 2D list representing maze tiles.

    Raises:
        QuitFromAppException: Raised if the user clicks the window's close button (X), indicating the app should quit.
    """
    running = True

    while running:
        # Handle user input
        for event in pygame.event.get():
            # User pressed X button
            if event.type == pygame.QUIT:
                raise QuitFromAppException()                
            
            # User pressed a key
            elif event.type == pygame.KEYDOWN:
                # Stop showing the maze
                if event.key == pygame.K_q:
                    running = False
                
                # Use dijkstra
                elif event.key == pygame.K_0:
                    dijkstra.solve(maze, screen, clock)
                    pause(screen, clock)
                    return
                
                # Use a *
                elif event.key == pygame.K_1:
                    astar.solve(maze, screen, clock)
                    pause(screen, clock)
                    return
                
                # Use q-learning
                elif event.key == pygame.K_2:
                    qlearning.solve(maze, screen, clock)
                    pause(screen, clock)
                    return
                
        # Draw the menu
        visual.drawSolutionMenu(screen)

        # Draw go back message
        mid_font = pygame.font.Font('./assets/font/main-font.ttf', size=15)
        go_back_label = mid_font.render('Go back to menu (Press q)', True, 'white')
        screen.blit(go_back_label, ((N_COLS*TILE_SIZE - go_back_label.get_width())//2, N_ROWS*TILE_SIZE-2*go_back_label.get_height()))

        pygame.display.flip()
        clock.tick(FPS)
