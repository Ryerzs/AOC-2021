import time
import numpy as np
import math
import matplotlib.pyplot as plt
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

    # Fit a second degree polynokmial to get good initial guess
    y = [calc_fuel_2(i, data) for i in range(3)]
    c = y[0]
    b = 2*y[1] -3*c/2 - y[2]/2
    a = y[1] -b -c
    mid = round(-b/(2*a))

    fuel_cost_2, mid_2 = calc_fuel(data, calc_fuel_2, mid-2, mid+2)

    # Fit a line to get an approximate initial guess
    y = [calc_fuel_1_no_abs(i, data) for i in range(2)]
    m = y[0]
    k = y[1] - m
    # our initial guess will be the root to the line
    # So we solve 'kx + m = 0'
    mid = round(-m/k)

    fuel_cost_1, mid_1 = calc_fuel(data, calc_fuel_1, mid-300, mid+300)

    dt = time.time() - start_time
    print(dt)
    print(fuel_cost_2, mid_2)
    print(round(mid_2))
    print(fuel_cost_1, mid_1)
    print(round(mid_1))

def calc_fuel(data, func, mi, ma):
    p = math.ceil(math.log(ma-mi, 2) )
    print(p)
    mid = mi + math.floor((ma-mi)/2)
    low = mi
    upp = ma
    fuel_cost = func(mid, data)
    for j in range(p):
        m1 = (mid - low)/2
        m2 = (upp - mid)/2
        f1 = func(mid - 1, data)
        f2 = func(mid + 1, data)
        if f1 < fuel_cost:
            upp = mid
            mid = upp - m1
            fuel_cost = func(mid, data)
        elif f2 < fuel_cost:
            low = mid
            mid = low + m2
            fuel_cost = func(mid, data)
        else:
            break
    return fuel_cost, mid

def calc_fuel_1(n, data):
    return sum([abs(n - i)*data[i] for i in range(len(data))])

def calc_fuel_2(n, data):
    return sum([abs(n-i)*(abs(n-i)+1)/2*data[i] for i in range(len(data))])

def calc_fuel_1_no_abs(n, data):
    return sum([(n - i)*data[i] for i in range(len(data))])

def calc_fuel_2_no_abs(n, data):
    return sum([(n-i)*(n-i+1)/2*data[i] for i in range(len(data))])

if __name__ == '__main__':
    main()
