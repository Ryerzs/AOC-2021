import time
import numpy as np
import math
def main():
    path = "data.txt"
    data_in = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()

    mi = min(data_in)
    ma = max(data_in)
    data = [0] * (ma + 1)
    # foreach squid at day i, increase index i by one
    for el in data_in:
        data[el] += 1
    p = math.ceil(math.log(ma, 2) )
    # Put centrum in middle
    mid = math.floor((ma-mi)/2)
    low = mi
    upp = ma
    fuel_cost = calc_fuel(mid, data)
    for j in range(p):
        m1 = (mid - low)/2
        m2 = (upp - mid)/2
        f1 = calc_fuel(mid - 1, data)
        f2 = calc_fuel(mid + 1, data)
        if f1 < fuel_cost:
            upp = mid
            mid = upp - m1
            fuel_cost = calc_fuel(mid, data)
        elif f2 < fuel_cost:
            low = mid
            mid = low + m2
            fuel_cost = calc_fuel(mid, data)
        else:
            break

    dt = time.time() - start_time
    print(dt)
    print(fuel_cost, mid)
    print(round(mid))

def calc_fuel(n, data):
    return sum([abs(n-i)*(abs(n-i)+1)/2*data[i] for i in range(len(data))])

if __name__ == '__main__':
    main()
