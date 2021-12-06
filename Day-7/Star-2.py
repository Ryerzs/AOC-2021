import time
import numpy as np

def main():
    path = "test-data.txt"
    data_in = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()

    dt = time.time() - start_time
    print(dt)

if __name__ == '__main__':
    main()