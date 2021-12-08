import time
import numpy as np

def main():
    path = "test-data.txt"
    data_in = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()

    ans1 = star1()
    ans2 = star2()

    dt = time.time() - start_time
    print(dt)
    print("Star 1:", ans1)
    print("Star 2:", ans2)

def star1():
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()