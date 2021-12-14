import time
import numpy as np

def main():
    path = "data.txt"
    # path = "test-data.txt"
    getting_points = True
    points = []
    folds = []
    for row in open(path, 'r').read().splitlines():
        if row == "":
            getting_points = False
            continue
        if getting_points:
            p = row.split(',')
            points.append((int(p[0]), int(p[1])))
        else:
            inst = row.split(' ')[2]
            inst = inst.split('=')
            if inst[0] == 'y':
                p = (0, int(inst[1]))
            else:
                p = (int(inst[1]), 0)
            folds.append(p)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    s = (max(x) + 1, max(y) + 1)
    grid = [[0 for i in range(s[0])] for j in range(s[1])]
    for p in points:
        grid[p[1]][p[0]] = 1
    
    start_time = time.time()
    for f in folds:
        if f[0] == 0:
            grid_upper = grid[0:f[1]]
            grid_lower = grid[f[1]+1:]
            rev_lower = []
            for i in range(len(grid_lower)-1,-1,-1):
                rev_lower.append(grid_lower[i])
            for i in range(len(rev_lower)):
                for j in range(len(rev_lower[0])):
                    grid_upper[i][j] = grid_upper[i][j] or rev_lower[i][j]
            grid = grid_upper
        else:
            new_grid = []
            for row in grid:
                new_r = []
                for (item1, item2) in zip(row[:f[0]], row[-1:-(f[0]+1):-1]):
                    new_r.append(item1 or item2)
                new_grid.append(new_r)
            grid = new_grid
    count = sum([sum([el > 0 for el in row]) for row in grid])

    dt = time.time() - start_time
    print(dt)
    print(count)
    for row in grid:
        s = ""
        for el in row:
            s = s + '#' * (not not el) + ' ' * (not el)
        print(s)

if __name__ == '__main__':
    main()