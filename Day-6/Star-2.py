import time
import numpy as np

def main():
    path = "test-data.txt"
    data_in = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()
    # Create data list
    data = [0 for i in range(9)]
    for el in data_in:
        data[el] += 1
    days = 256
    # Iterate through each day
    for i in range(days):
        # Pop previous day, essentially shifting all days forward
        new = data.pop(0)
        # Add the amount that was on the previous day to day 6
        # and to new squids
        data[6] += new
        data.append(new)
    dt = time.time() - start_time
    print(dt)
    print(sum(data))

if __name__ == '__main__':
    main()