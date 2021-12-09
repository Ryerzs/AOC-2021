import time
from Board import *

def main():
    path = "data.txt"
    data = [[int(el) for el in row] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    N = 10
    for i in range(N):
        board = Board(data)
        low_points = board.find_low_points()
        ans1 = star1(board)
        ans2 = star2(board, low_points)

    dt = (time.time() - start_time)/N

    print(dt)
    # ~80ms
    print("Star 1:", ans1)
    print("Star 2:", ans2)

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



if __name__ == '__main__':
    main()