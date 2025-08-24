from maze.app.consts import FPS, N_COLS, TILE_SIZE, N_ROWS
import maze.app.visualizer as visual
import pygame

class QuitFromAppException(Exception):
    """
    Custom exception to indicate that the user wants to quit the application.

    This is raised when the user clicks the window's close button (X).
    """
    
    def __init__(self, *args):
        super().__init__(*args)

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
                if event.key == pygame.K_0:
                    running = False
                    break

        # Show the maze
        visual.drawMaze(screen, maze)

        # Draw go back message
        mid_font = pygame.font.Font('./assets/font/main-font.ttf', size=15)
        go_back_label = mid_font.render('Go back to menu (Press 0)', True, 'white')
        screen.blit(go_back_label, ((N_COLS*TILE_SIZE - go_back_label.get_width())//2, N_ROWS*TILE_SIZE-2*go_back_label.get_height()))

        pygame.display.flip()
        clock.tick(FPS)

def generateMaze(screen, clock):
    ...

def solveMaze(screen, clock, maze):
    ...
