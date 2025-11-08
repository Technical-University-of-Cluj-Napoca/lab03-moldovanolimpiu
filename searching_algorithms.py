from queue import PriorityQueue
from grid import Grid
from spot import Spot
from collections import deque
import pygame
import time

def bfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Breadth-First Search (BFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    if start == None or end == None:
        return False
    
    queue = deque()
    queue.append(start)
    visited = {start}
    came_from = {}

    while len(queue) != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.popleft()
        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False

def dfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Depth-First Search (DFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    if start == None or end == None:
        return False

    stack = [start]
    visited = {start}
    came_from = {}

    while len(stack) !=0:


        current = stack.pop()
        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
                neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False

def astar(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    """
    A* Pathfinding Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        None
    """
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0,count,start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid.grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score[start] = h(start.get_position(), end.get_position())

    lookup_set = {start}

    while not open_heap.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_heap.get()[2]
        lookup_set.remove(current)

        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())
                if neighbor not in lookup_set:
                    count+=1
                    open_heap.put((f_score[neighbor],count,neighbor))
                    lookup_set.add(neighbor)
                    neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()

    return False

def h(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    """
    Heuristic function for A* algorithm: uses the Manhattan distance between two points.
    Args:
        p1 (tuple[int, int]): The first point (x1, y1).
        p2 (tuple[int, int]): The second point (x2, y2).
    Returns:
        float: The Manhattan distance between p1 and p2.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 -x2) + abs(y1-y2)


def dls(draw: callable, grid: Grid, start: Spot, end: Spot, lim: int) -> bool:
    
    stack = [(start,0)]
    visited = {start}
    came_from = {}
  

    while len(stack) !=0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current ,depth= stack.pop()
        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier() and depth+1 <= lim:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append((neighbor,depth+1))
                neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
            
    return False

def IDDFS(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    for i in range(0,200):
        if dls(lambda: grid.draw(),grid,start,end,i) == True:
            return True
        
    return False

def UCS(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    if start == None or end == None:
        return False
    
    priority_queue = PriorityQueue()
    priority_queue.put((0,start))
    came_from = {}
    visited = {start: 0}

    while not priority_queue.empty() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_cost, current_node = priority_queue.get()

        if current_node == end:
            while current_node in came_from:
                current_node = came_from[current_node]
                current_node.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in  current_node.neighbors:
            total_cost = current_cost + 1
            
            if neighbor not in visited or total_cost < visited[neighbor]:
                visited[neighbor] = total_cost
                came_from[neighbor] = current_node
                priority_queue.put((total_cost, neighbor))
                neighbor.make_open()
        draw()

        if current_node != start:
            current_node.make_closed()
    return False
    
def Dijkstra(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    priority_queue = PriorityQueue()
    dist = {spot: float("inf") for row in grid.grid for spot in row}
    dist[start] = 0
    came_from = {}
    priority_queue.put((0, start))

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current_cost, current_node = priority_queue.get()

        if current_cost > dist[current_node]:
            continue

        if current_node == end:
            while current_node in came_from:
                current_node = came_from[current_node]
                current_node.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current_node.neighbors:
            total_cost = current_cost + 1

            if dist[neighbor] > total_cost:
                dist[neighbor] = total_cost
                came_from[neighbor] = current_node
                priority_queue.put((total_cost,neighbor))
                neighbor.make_open()
        draw()
        if current_node != start:
            current_node.make_closed()

    return False

def IDAS(draw: callable, grid: Grid, start: Spot, end: Spot, lim: int) -> bool:
    """
    A* Pathfinding Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        None
    """
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0,count,start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid.grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score[start] = h(start.get_position(), end.get_position())

    lookup_set = {start}

    while not open_heap.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_heap.get()[2]
        lookup_set.remove(current)

        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())
                if neighbor not in lookup_set and f_score[neighbor] <= lim:
                    count+=1
                    open_heap.put((f_score[neighbor],count,neighbor))
                    lookup_set.add(neighbor)
                    neighbor.make_open()
        draw()

        if current != start:
            current.make_closed()

    return False

def IDASfor(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    for i in range(20,1000):
        if IDAS(lambda: grid.draw(), grid, start, end,i) == True:
            return True
    
    return False