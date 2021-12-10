import time
from Board import *

def main():
    path = "test-data.txt"
    data = [[int(el) for el in row] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    N = 1
    for i in range(N):
        board = Board(data)
        low_points = board.find_low_points()
        ans1 = star1(board)
        ans2 = star2(board, low_points)
        data_2 = [row for row in open(path, 'r').read().splitlines()]
        ans2_alt = star2_alt(data_2)

    dt = (time.time() - start_time)/N

    print(dt)
    # ~80ms
    print("Star 1:", ans1)
    print("Star 2:", ans2)
    print("Star 2 alternate:", ans2_alt)

def star1(board):
    return board.low_points_value

def star2(board, low_points):
    basin_lengths = []
    for p in low_points:
        basin_lengths.append(board.find_basin_length(p))
    prod = 1
    for i in range(3):
        b_max = max(basin_lengths)
        basin_lengths.remove(b_max)
        prod *= b_max
    return prod

def star2_alt(data):
    row = data[0]
    print(row)
    sub = row.split('9')
    print(sub)
    basins = []
    for el in sub:
        if len(basins) == 0:
            basins.append(set(range(0, len(el))))
            prev = len(el) + 1
            continue
        if len(el) == 0:
            prev += 1
            continue
        basins.append(  set(range(prev, prev + len(el))) )
        prev = prev + 1 + len(el)
    print(basins)
    r1 = set(range(0,2))
    r2 = set(range(1,5))
    print(r1 & r2)
    return 0


if __name__ == '__main__':
    main()