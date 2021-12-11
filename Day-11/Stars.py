import time
from Board import *

def main():
    path = "data.txt"
    data = [[int(el) for el in row] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    N = 1
    for i in range(N):
        board = Board(data)
        board.step(step = 100)
        flash_count = board.flash_count
        ind = board.step(step = 200) + 100

    dt = (time.time() - start_time)/N

    print(dt)
    print(flash_count)
    print(ind)

if __name__ == '__main__':
    main()