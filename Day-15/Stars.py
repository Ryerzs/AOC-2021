import time
import numpy as np
from collections import deque
from Board import *

def main():
    path = "data.txt"
    # path = "test-data.txt"
    grid_1 = [[int(el) for el in row] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()

    s = (len(grid_1), len(grid_1[0]))
    grid_2 = increment_grid(grid_1)
    grid_3 = increment_grid(grid_2)
    grid_4 = increment_grid(grid_3)
    grid_5 = increment_grid(grid_4)
    grid_6 = increment_grid(grid_5)
    grid_7 = increment_grid(grid_6)
    grid_8 = increment_grid(grid_7)
    grid_9 = increment_grid(grid_8)
    grids = [[grid_1, grid_2, grid_3, grid_4, grid_5],
             [grid_2, grid_3, grid_4, grid_5, grid_6],
             [grid_3, grid_4, grid_5, grid_6, grid_7],
             [grid_4, grid_5, grid_6, grid_7, grid_8],
             [grid_5, grid_6, grid_7, grid_8, grid_9]]
    grid = []
    for j in range(len(grids)):
        for i in range(s[0]):
            row = []
            for g in grids[j]:
                row += g[i]
            grid.append(row)

            
    # print(grid)

    # for row in grid:
    #     s = ''
    #     for el in row:
    #         s += str(el)
    #     print(s)

    s = (len(grid), len(grid[0]))
    board = Board(s, grid)
    board.print_grid()
    
    start = board.grid[0][0]
    end = board.grid[board.s[0]-1][board.s[1]-1]
    openSet = deque([start])
    gScore = {}
    fScore = {}
    for i in range(board.s[0]):
        for j in range(board.s[1]):
            gScore[board.grid[i][j]] = board.s[0] * board.s[1] * 10
            fScore[board.grid[i][j]] = 2 * ((board.s[0] * board.s[1])**2) * 10
    cameFrom = {}
    gScore[start] = 0
    fScore[start] = h(start, end)
    path = None
    while openSet:
        current = openSet[0]
        for node in openSet:
            if fScore[node] < fScore[current]:
                current = node
        if current == end:
            path = reconstruct_path(cameFrom, current)
            break
    
        # print(current.ind)
        # current.print_neighbors()
        openSet.remove(current)
        for n in current.neigh:
            tentative_gScore = gScore[current] + n.val   
            if tentative_gScore < gScore[n]:
                cameFrom[n] = current
                gScore[n] = tentative_gScore
                fScore[n] = tentative_gScore + h(n, end)
                if n not in openSet:
                    openSet.append(n)
    print_path(path)
    grid = make_grid_from_path(path, board.s)
    for row in grid:
        print(''.join(row))
    
    print(gScore[end])

    ans1 = star1()
    ans2 = star2()

    dt = time.time() - start_time
    print(dt)
    print("Star 1:", ans1)
    print("Star 2:", ans2)

def increment_grid(grid):
    s = (len(grid), len(grid[0]))
    new = [[0 for j in range(s[1])] for i in range(s[0])]
    for i in range(s[0]):
        for j in range(s[1]):
            new[i][j] = grid[i][j]%9 + 1
    return new

def make_grid_from_path(path, s):
    grid = [[' ' for j in range(s[1])] for i in range(s[0])]
    for p in path:
        grid[p.ind[0]][p.ind[1]] = str(p.val)
    return grid

def print_path(path):
    for p in path:
        print(p.ind)

def h(node, end):
    return abs(node.ind[0] - end.ind[0]) + abs(node.ind[1] - end.ind[1])

def reconstruct_path(cameFrom, current):
    total_path = deque([current])
    while current in cameFrom:
        current = cameFrom[current]
        total_path.appendleft(current)
    return total_path

def star1():
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()