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
    fuel_cost = sum([abs(mid - i)*data[i] for i in range(len(data))])
    for j in range(p+3):
        m1 = math.floor((mid - low)/2)
        m2 = math.ceil((upp - mid)/2)
        # m1 = (mid - low)/2
        # m2 = (upp - mid)/2
        f1 = sum([abs(mid - i - 1)*data[i] for i in range(len(data))])
        f2 = sum([abs(mid - i + 1)*data[i] for i in range(len(data))])
        # print(f1, f2, fuel_cost)
        # print(m1, m2, low, upp, mid)
        # print("")
        if f1 < fuel_cost:
            upp = mid
            mid = upp - m1
            fuel_cost = sum([abs(mid - i)*data[i] for i in range(len(data))])
        elif f2 < fuel_cost:
            low = mid
            mid = low + m2
            fuel_cost = sum([abs(mid - i)*data[i] for i in range(len(data))])
        else:
            break

    # fuel_cost = []   
    # for j in range(ma + 1):
    #     fuel_cost.append(sum([abs(j - i)*data[i] for i in range(len(data))]))
    # min_f = min(fuel_cost)
    # index_min = np.argmin(fuel_cost)
    # print(min_f, index_min)

    dt = time.time() - start_time
    print(dt)
    print(fuel_cost, mid)
    print(round(mid))

if __name__ == '__main__':
    main()
