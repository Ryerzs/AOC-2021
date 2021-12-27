import time
from Graph import *

def main():
    path = "data.txt"
    path = "test-data.txt"

    data = []
    start_time = time.perf_counter()
    with open(path) as f:
        rows = f.read().splitlines()
        for r in rows:
            row = []
            for cv in r:
                row.append(10**(ord(cv) - 65))
            data.append(row)

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2()
    time3 = time.perf_counter()

    load_time = time1 - start_time
    star1_time = time2 - time1
    star2_time = time3 - time2
    if 1:
        print(f'Load time: {load_time}')
        print(f'Star 1 time: {star1_time}')
        print(f'Star 2 time: {star2_time}')
        print(f'Star 1 answer: {ans1}')
        print(f'Star 2 answer: {ans2}')

def star1(data):
    roomSize = len(data)
    g = Graph(roomSize, data)
    print(len(g.points))
    # ds1 = distToSpace(1, 3, roomSize, data[1][0])
    # ds2 = distToSpace(0, -1, roomSize, data[0][0])
    # print(ds)
    # spaces = [-2, -1, 0, 1, 2, 3, 4]

def distToSpace(fr, to, roomSize, val):
    ind = fr * 2
    ind1 = ind - 1 
    ind2 = ind + 1 
    return (abs(ind-to) + roomSize) * val

def star2():
    return 0

if __name__ == '__main__':
    main()