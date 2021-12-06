import time
import numpy as np

def main():
    path = "data.txt"
    # data = [row.split(",") for row in open(path, 'r').read().splitlines()]
    data = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()
    days = 80
    for i in range(days):
        new = sum([1 for el in data if el == 0])
        data = [s-1 if s>0 else 6 for s in data]
        for j in range(new):
            data.append(8)

    dt = time.time() - start_time
    print(dt)
    print(len(data))

if __name__ == '__main__':
    main()