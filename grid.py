from utils import COLORS
from spot import Spot
import pygame
from bttn import Button

class Grid:
    def __init__(self, win: pygame.Surface, rows: int, cols: int, width: int, height: int):
        """
        Initialize a grid with the given number of rows and columns, of the width and height of the window.
        Args:
            win (pygame.Surface): The Pygame surface (window) where the grid will be drawn.
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            width (int): Width of the window in pixels.
            height (int): Height of the window in pixels.
        """
        self.win: pygame.Surface = win
        self.rows: int = rows
        self.cols: int = cols
        self.width: int = width
        self.height: int = height
        self.grid: list[list[Spot]] = self._make_grid()

        self.bfs_button = Button(950, 100, 200, 50, "BFS", self.bfs_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.dfs_button = Button(950, 160, 200, 50, "DFS", self.dfs_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.dls_button = Button(950, 220, 200, 50, "DLS", self.dls_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.ucs_button = Button(950, 280, 200, 50, "UCS", self.ucs_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.dijkstra_button = Button(950, 340, 200, 50, "DIJKSTRA", self.dijkstra_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.astar_button = Button(950, 400, 200, 50, "A*", self.astar_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.IDDFS_button = Button(950, 460, 200, 50, "IDDFS", self.IDDFS_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.IDAS_button = Button(950, 520, 200, 50, "IDAS", self.IDAS_action, COLORS["BUTTON GRAY"], COLORS["GREEN"],font = None)
        self.reset_button = Button(950, 580, 200, 50, "RESET", self.reset, COLORS["RED"], COLORS["WHITE"],font = None)

        self.reset_clicked = False
        self.algorithm_clicked = [False] * 8
        self.algorithm_clicked[0] = True

        self.indicator = pygame.Rect(930, 110, 15, 15)




    def _make_grid(self) -> list[list[Spot]]:
        """
        Create a grid of Spot objects.
        Returns:
            list[list[Spot]]: A 2D list (matrix) representing the grid of Spot objects.
        """
        grid = []
        spot_width = self.width // self.rows  # width of each spot
        spot_height = self.height // self.cols  # height of each spot
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                spot = Spot(i, j, spot_width, spot_height, self.rows)
                grid[i].append(spot)
        return grid

    def draw_grid_lines(self) -> None:
        """
        Draw the grid lines on the Pygame window.
        Returns:
            None
        """
        spot_width = self.width // self.rows  # gap between lines
        spot_height = self.height // self.cols  # gap between lines
        # for i in range(self.rows):
        #     # draw horizontal lines
        #     pygame.draw.line(self.win, COLORS['GREY'], (0, i * spot_height), (self.width, i * spot_height))
        #     for j in range(self.cols):
        #         # draw vertical lines
        #         pygame.draw.line(self.win, COLORS['GREY'], (j * spot_width, 0), (j * spot_width, self.height))
        for i in range(self.rows):
            # draw horizontal lines
            pygame.draw.line(self.win, COLORS['GREY'], (0, i * spot_height), (self.width, i * spot_height))
        for j in range(self.cols+1):
            # draw vertical lines
            pygame.draw.line(self.win, COLORS['GREY'], (j * spot_width, 0), (j * spot_width, self.height))
    
    def buttonIndRed(self):
        self.bfs_button.setColorIndicatorRed()
        self.dfs_button.setColorIndicatorRed()
        self.dls_button.setColorIndicatorRed()
        self.ucs_button.setColorIndicatorRed()
        self.dijkstra_button.setColorIndicatorRed()
        self.astar_button.setColorIndicatorRed()
        self.IDAS_button.setColorIndicatorRed()
        self.IDDFS_button.setColorIndicatorRed()

    def reset_list(self):
        for i in range(0,8):
            self.algorithm_clicked[i] = False
    def reset_grid(self):
        print("clicked")
    def bfs_action(self):
        print("BFSclicked")
        self.reset_list()
        self.algorithm_clicked[0] = True
        self.buttonIndRed()
        self.bfs_button.setColorIndicatorGreen()
    def dfs_action(self):
        print("DFSclicked")
        self.reset_list()
        self.algorithm_clicked[1] = True
        self.buttonIndRed()
        self.dfs_button.setColorIndicatorGreen()
    
    def dls_action(self):
        print("DLSclicked")
        self.reset_list()
        self.algorithm_clicked[2] = True
        self.buttonIndRed()
        self.dls_button.setColorIndicatorGreen()
    
    def ucs_action(self):
        print("UCSclicked")
        self.reset_list()
        self.algorithm_clicked[3] = True
        self.buttonIndRed()
        self.ucs_button.setColorIndicatorGreen()
 
    def dijkstra_action(self):
        print("DIJclicked")
        self.reset_list()
        self.algorithm_clicked[4] = True
        self.buttonIndRed()
        self.dijkstra_button.setColorIndicatorGreen()
    
    def astar_action(self):
        print("ASclicked")
        self.reset_list()
        self.algorithm_clicked[5] = True
        self.buttonIndRed()
        self.astar_button.setColorIndicatorGreen()

    def IDDFS_action(self):
        print("IDFSclicked")
        self.reset_list()
        self.algorithm_clicked[6] = True
        self.buttonIndRed()
        self.IDDFS_button.setColorIndicatorGreen()
    
    def IDAS_action(self):
        print("IDASclicked")
        self.reset_list()
        self.algorithm_clicked[7] = True
        self.buttonIndRed()
        self.IDAS_button.setColorIndicatorGreen()
 

    
    def draw(self) -> None:
        """
        Draw the entire grid and its spots on the Pygame window.
        Returns:
            None
        """
        self.win.fill(COLORS['MENU GRAY'])  # fill the window with white color
        

        for row in self.grid:
            for spot in row:
                spot.draw(self.win)   # draw each spot

        self.draw_grid_lines()        # draw the grid lines  
        self.reset_button.draw(self.win)  
        self.bfs_button.draw(self.win)    
        self.dfs_button.draw(self.win) 
        self.dls_button.draw(self.win)   
        self.ucs_button.draw(self.win) 
        self.dijkstra_button.draw(self.win) 
        self.astar_button.draw(self.win)
        self.IDDFS_button.draw(self.win)
        self.IDAS_button.draw(self.win)
        #pygame.draw.rect(self.win,COLORS['RED'],self.indicator)
        pygame.display.update()       # update the display

    def get_clicked_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        """
        Get the row and column of the grid based on the mouse position.
        Args:
            pos (tuple[int, int]): The (x, y) position of the mouse click.
        Returns:
            tuple[int, int]: The (row, col) position of the clicked spot in the grid.
        """
        spot_width = self.width // self.cols
        spot_height = self.height // self.rows
        x, y = pos
        col = x // spot_width
        row = y // spot_height
        return col, row
    
    def reset(self) -> None:
        """
        Reset the grid to its initial state.
        Returns:
            None
        """
        for row in self.grid:
            for spot in row:
                spot.reset()
        self.reset_clicked = True
        
    def clearPrior(self) -> None:
        for row in self.grid:
            for spot in row:
                if (not spot.is_barrier()) and (not spot.is_start()) and (not spot.is_end()):
                    spot.reset()
    