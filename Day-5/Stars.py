import time
from Board import *
import numpy as np

def main():
    # ~97ms
    print("Star 1:")
    star1()
    # ~153ms
    print("Star 2:")
    star2()
    # ~229ms
    print("Both:")
    stars()

def star1():
    path = "Day-5\data.txt"
    rows = [row for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    lines = [[[int(point) for point in coord.split(",")] for coord in row.split(" -> ")] for row in rows]
    # Numpy to find absolute max value in lines
    s = np.max(lines)
    # Create board of size s+1 x s+1
    board = Board(s+1)
    for i in range(len(lines)):
        board.add_line(lines[i], False)
    count = board.get_overlap_count()
    dt = time.time() - start_time
    print(dt)
    print(count)

def star2():
    path = "Day-5\data.txt"
    rows = [row for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    lines = [[[int(point) for point in coord.split(",")] for coord in row.split(" -> ")] for row in rows]
    # Numpy to find absolute max value in lines
    s = np.max(lines)
    # Create board of size s+1 x s+1
    board = Board(s+1)
    for i in range(len(lines)):
        board.add_line(lines[i], True)
    count = board.get_overlap_count()
    dt = time.time() - start_time
    print(dt)
    print(count)

def stars():
    path = "Day-5\data.txt"
    rows = [row for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    lines = [[[int(point) for point in coord.split(",")] for coord in row.split(" -> ")] for row in rows]
    # Numpy to find absolute max value in lines
    s = np.max(lines)
    # Create board of size s+1 x s+1
    board = Board(s+1)
    for i in range(len(lines)):
        board.add_line(lines[i], False)
    count = board.get_overlap_count()
    board = Board(s+1)
    for i in range(len(lines)):
        board.add_line(lines[i], True)
    count = board.get_overlap_count()
    dt = time.time() - start_time
    print(dt)

if __name__ == "__main__":
    main()