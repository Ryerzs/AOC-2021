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

    fuel_cost_1, mid_1 = calc_fuel(data, calc_fuel_1, mi, ma)
    fuel_cost_2, mid_2 = calc_fuel(data, calc_fuel_2, mi, ma)

    print(fuel_cost_1, mid_1)
    print(round(mid_1))
    print(fuel_cost_2, mid_2)
    print(round(mid_2))

    y = [calc_fuel_2(i, data) for i in range(3)]
    c = y[0]
    b = 2*y[1] -3*c/2 - y[2]/2
    a = y[1] -b -c
    mid = -b/(2*a)
    print(mid)

    # fuel_cost_1_1 = calc_fuel_all(data, calc_fuel_1_na, mi, ma)
    # fuel_cost_1_2 = calc_fuel_all(data, calc_fuel_1_n, mi, ma)
    # x = [fuel_cost_1_1[i][0] for i in range(len(fuel_cost_1_1))]
    # y = [fuel_cost_1_1[i][1] for i in range(len(fuel_cost_1_1))]
    # plt.plot(x, y)
    # x = [fuel_cost_1_2[i][0] for i in range(len(fuel_cost_1_2))]
    # y = [fuel_cost_1_2[i][1] for i in range(len(fuel_cost_1_2))]
    # plt.plot(x, y)
    # plt.savefig("plot_star_1.pdf")
    # plt.close()

    # fuel_cost_2_1 = calc_fuel_all(data, calc_fuel_2_na, mi, ma)
    # fuel_cost_2_2 = calc_fuel_all(data, calc_fuel_2_n, mi, ma)
    # x = [fuel_cost_2_1[i][0] for i in range(len(fuel_cost_2_1))]
    # y = [fuel_cost_2_1[i][1] for i in range(len(fuel_cost_2_1))]
    # plt.plot(x, y)
    # x = [fuel_cost_2_2[i][0] for i in range(len(fuel_cost_2_2))]
    # y = [fuel_cost_2_2[i][1] for i in range(len(fuel_cost_2_2))]
    # plt.plot(x, y)
    # plt.savefig("plot_star_2.pdf")
    # plt.close()

    # print(fuel_cost_1, mid_1)
    # print(round(mid_1))
    # print(fuel_cost_2, mid_2)
    # print(round(mid_2))

    dt = time.time() - start_time
    print(dt)

def calc_fuel_all(data, func, mi, ma):
    fuel = []
    x = [i for i in range(-2000, 3000)]
    for i in x:
        fuel.append([i, func(i, data)])
    return fuel

def calc_fuel(data, func, mi, ma):
    p = math.ceil(math.log(ma, 2) )
    mid = math.floor((ma-mi)/2)
    low = mi
    upp = ma
    fuel_cost = func(mid, data)
    for j in range(p+3):
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

def calc_fuel_1_na(n, data):
    return sum([(n - i)*data[i] for i in range(len(data))])

def calc_fuel_2_na(n, data):
    return sum([(n-i)*(n-i+1)/2*data[i] for i in range(len(data))])

def calc_fuel_1_n(n, data):
    return sum([abs(n - i)*data[i] for i in range(len(data))])

def calc_fuel_2_n(n, data):
    return sum([abs(n-i)*(abs(n-i)+1)/2*data[i] for i in range(len(data))])

if __name__ == '__main__':
    main()
