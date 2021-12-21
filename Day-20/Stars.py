import time
from collections import defaultdict
import copy

def main():
    path = "data.txt"
    # path = "test-data.txt"
    # path = "test-data2.txt"

    data = []
    start_time = time.perf_counter()
    alg, pict, size = getData(path)

    one = defaultdict(oneDefault)
    zero = defaultdict(zeroDefault)
    global typeOne
    typeOne = one.default_factory
    global typeZero
    typeZero = zero.default_factory

    test()

    time1 = time.perf_counter()

    pictCopy = copy.deepcopy(pict)
    sizeCopy = copy.deepcopy(size)
    ans1 = star1(alg, pict, size)
    time2 = time.perf_counter()

    ans2 = star2(alg, pictCopy, sizeCopy)
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

def test():
    d = defaultdict(zeroDefault)
    d[4] = 1
    print(d[4])
    print(d[1])
    print(d.default_factory)
    b = d.default_factory
    print(b)
    if d.default_factory  == b:
        print('yes')

def zeroDefault():
    return 0

def oneDefault():
    return 1

def getData(path):
    pict = defaultdict(zeroDefault)
    size = []
    with open(path) as f:
        rows = f.read().splitlines()
        alg = ''
        for cv in rows[0]:
            val = '1' if cv == '#' else '0'
            alg = alg + val
        rows = rows[2:]
        for y, r in enumerate(rows):
            for x, cv in enumerate(r):
                val = 0
                if cv == '#':
                    val = 1
                pict[(x,y)] = val
        size = [[0,x+1], [0,y+1]]
    return alg, pict, size

def star1(alg, pict, size):
    N = 2
    printPict(pict, size)
    for i in range(N):
        pict, size = pictureStep(alg, pict, size)
    printPict(pict, size)
    count = 0
    for key, val in pict.items():
        count += val
    return count

def pictureStep(alg, pict, size):
    xSize = size[0]
    ySize = size[1]
    newxSize = [xSize[0] -1, xSize[1] + 1]
    newySize = [ySize[0] -1, ySize[1] + 1]
    newSize = [newxSize, newySize]
    # print(newSize)
    pairs = get3b3(newSize)
    if alg[0] == '1' and pict.default_factory == typeZero:
        newPict = defaultdict(oneDefault)
    else:
        newPict = defaultdict(zeroDefault)
    for pair in pairs:
        pairVal = getPairVal(pair, pict)
        pictVal = getPictVal(pairVal, alg)
        # print(pairVal, pictVal)
        newPict[pair[4]] = pictVal
    return newPict, newSize

def getPictVal(pairVal, alg):
    return int(alg[pairVal])

def getPairVal(pair, pict):
    pointRow = ''
    for point in pair:
        pointRow = pointRow + str(pict[point])
    return int(pointRow, 2)

def get3b3(size):
    pairs = []
    for y in range(size[1][0], size[1][1]):
        for x in range(size[0][0], size[0][1]):
            adj = getSurroundingIndex(x, y)
            pairs.append(adj)
    return pairs

def getSurroundingIndex(i, j):
    adj = [
        (i - 1, j - 1),
        (i    , j - 1),
        (i + 1, j - 1),
        (i - 1, j    ),
        (i    , j    ),
        (i + 1, j    ),
        (i - 1, j + 1),
        (i, j + 1    ),
        (i + 1, j + 1),
    ]
    return adj

def printPict(pict, size):
    xSize = size[0]
    ySize = size[1]
    grid = []
    lenx = xSize[1] - xSize[0] + 2
    leny = ySize[1] - ySize[0] + 2
    lowx = xSize[0] - 1
    lowy = ySize[0] - 1
    for y in range(leny):
        grid.append([' ']*lenx)
    for key, val in pict.items():
        x = key[0] - lowx
        y = key[1] - lowy
        c = ' '
        if val:
            c = '#'
        grid[y][x] = c
    for row in grid:
        string = ''.join(row)
        print(string)

def star2(alg, pict, size):
    N = 50
    printPict(pict, size)
    for i in range(N):
        pict, size = pictureStep(alg, pict, size)
    printPict(pict, size)
    count = 0
    for key, val in pict.items():
        count += val
    return count

if __name__ == '__main__':
    main()