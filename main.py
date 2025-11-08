import pygame
from utils import WIDTH, HEIGHT
#from queue import PriorityQueue
from grid import Grid
#from spot import Spot
#from collections import deque
from utils import COLORS
import time
from bttn import Button
from searching_algorithms import bfs, dfs, dls, UCS, astar, Dijkstra, IDASfor, IDDFS

# setting up how big will be the display window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set a caption for the window
pygame.display.set_caption("Path Visualizing Algorithm")


if __name__ == "__main__":
    ROWS = 50  # number of rows
    COLS = 50  # number of columns
    grid = Grid(WIN, ROWS, COLS, 800, HEIGHT)

    start = None
    end = None
    

    # flags for running the main loop
    run = True
    started = False

    pygame.mixer.music.load('sounds/banditradio.mp3')

    pygame.mixer.music.play(-1,0.0)

    while run:
        grid.draw()  # draw the grid and its spots
        
        for event in pygame.event.get():
            # verify what events happened
            if event.type == pygame.QUIT:
                run = False
            grid.reset_button.handle_event(event)
            grid.bfs_button.handle_event(event) #0
            grid.dfs_button.handle_event(event) #1
            grid.dls_button.handle_event(event) #2
            grid.ucs_button.handle_event(event) #3
            grid.dijkstra_button.handle_event(event) #4
            grid.astar_button.handle_event(event) #5
            grid.IDDFS_button.handle_event(event) #6
            grid.IDAS_button.handle_event(event) #7

            if grid.algorithm_clicked[0] == True:
                grid.bfs_button.setColorIndicatorGreen()
            if grid.reset_clicked == True:
                start = None
                end = None
                grid.reset_clicked = False
            
            

            if started:
                # do not allow any other interaction if the algorithm has started
                continue  # ignore other events if algorithm started

            if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                if row >= ROWS or row < 0 or col >= COLS or col < 0:
                    continue  # ignore clicks outside the grid
                spot = grid.grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # RIGHT CLICK
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                spot = grid.grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    # run the algorithm
                    grid.clearPrior()
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    
                    # TODO
                    #IDDFS(lambda: grid.draw(), grid, start, end)
                    #IDASfor(lambda: grid.draw(), grid, start, end)
                    #astar(lambda: grid.draw(), grid, start, end)
                    #IDASfor(lambda: grid.draw(), grid, start, end)

                    if grid.algorithm_clicked[0] == True:
                        bfs(lambda: grid.draw(), grid, start, end)
                        
                    elif grid.algorithm_clicked[1] == True:
                        dfs(lambda: grid.draw(), grid, start, end)
                    elif grid.algorithm_clicked[2] == True:
                        dls(lambda: grid.draw(), grid, start, end,100)
                    elif grid.algorithm_clicked[3] == True:
                        UCS(lambda: grid.draw(), grid, start, end)
                    elif grid.algorithm_clicked[4] == True:
                        Dijkstra(lambda: grid.draw(), grid, start, end)
                    elif grid.algorithm_clicked[5] == True:
                        astar(lambda: grid.draw(), grid, start, end)
                    elif grid.algorithm_clicked[6] == True:
                        IDDFS(lambda: grid.draw(), grid, start, end)
                    elif grid.algorithm_clicked[7] == True:
                        IDASfor(lambda: grid.draw(), grid, start, end)
                    

                    started = False
                    # call the algorithm
                    # grid.a_star_algorithm(lambda: grid.draw(), start, end)

                if event.key == pygame.K_c:
                    print("Clearing the grid...")
                    start = None
                    end = None
                    grid.reset()

        
    pygame.quit()
