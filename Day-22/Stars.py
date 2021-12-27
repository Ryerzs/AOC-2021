import time
from collections import defaultdict
from Box import *

def main():
    path = "data.txt"
    path = "test-data.txt"
    path = "test-data2.txt"

    data = []
    start_time = time.perf_counter()
    data = getData(path)

    # test()

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2(data)
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

def getData(path):
    with open(path) as f:
        rows = f.read().splitlines()
        instructions = []
        for r in rows:
            split = r.split(' ')
            val = 1 if split[0] == 'on' else 0
            coordRange = []
            for coord in split[1].split(','):
                trimmed = coord[2:]
                lower = int(trimmed.split('..')[0])
                upper = int(trimmed.split('..')[1])
                coordRange.append([lower, upper])
            instructions.append([val, coordRange])
        return instructions

def test():
    r = range(0,1)
    print(len(r))
    exit()

def star1(data):
    grid = defaultdict(zeroDefault)
    for i, inst in enumerate(data):
        print(i)
        flipGrid(grid, inst[0], inst[1])
    count = 0
    for key, val in grid.items():
        count += val
    print(count)
    return 0

def flipGrid(grid, val, ranges):
    xRange = range(ranges[0][0], ranges[0][1] + 1)
    yRange = range(ranges[1][0], ranges[1][1] + 1)
    zRange = range(ranges[2][0], ranges[2][1] + 1)
    for x in xRange:
        for y in yRange:
            for z in zRange:
                grid[(x,y,z)] = val

def dictFactoryType(dic, n):
    one = defaultdict(oneDefault)
    zero = defaultdict(zeroDefault)
    oneType = one.default_factory
    zeroType = zero.default_factory
    if n == 0:
        return dic.default_factory == zeroType 
    elif n == 1:
        return dic.default_factory == oneType 
    return None

def zeroDefault():
    return 0

def oneDefault():
    return 1

def star2(data):
    boxes = []
    for inst in data:
        val = inst[0]
        ranges = inst[1]
        boxes.append(Box(val, ranges))
    print(boxes[0].getVolume())
    print(boxes[1].getVolume())
    newBoxes = overlapping(boxes[0], boxes[1])
    s = 0
    b1 = newBoxes[0]
    print(b1.xRange, b1.yRange, b1.zRange, b1.getVolume())
    for b in newBoxes:
        s += b.getVolume()
    print(s)
    return 0

def overlapping(box1, box2):
    boxes = []
    interx1 = box1.getIntervall(0)
    print(interx1)
    interx2 = box2.getIntervall(0)
    newx = getNewRange(interx1, interx2)
    print(newx)
    intery1 = box1.getIntervall(1)
    intery2 = box2.getIntervall(1)
    newy = getNewRange(intery1, intery2)
    print(newy)
    interz1 = box1.getIntervall(2)
    interz2 = box2.getIntervall(2)
    newz = getNewRange(interz1, interz2)
    print(newz)
    for i, x in enumerate([newx, interx1]):
        for j, y in enumerate([newy, intery1]):
            for k, z in enumerate([newz, interz1]):
                if i and j and k:
                    continue
                rx = [x[0], x[-1]]
                ry = [y[0], y[-1]]
                rz = [z[0], z[-1]]
                print(rx, ry, rz)
                b = Box(1, [rx, ry, rz])
                if b.getVolume() != 0:
                    boxes.append(b)
    return boxes

def getNewRange(r1, r2):
    if r1[0] == r2[0] and r1[1] == r2[1]:
        return [0, 0]
    if r1[0] == r2[0] and r1[0] == r2[1]:
        return [r1[0] + 1, r1[1]]
    if r1[0] < r2[0] <= r1[1]:
        return [r1[0], r2[0] - 1]
    if r1[0] <= r2[1] <= r1[1]:
        return [r2[1] + 1, r1[1]]

if __name__ == '__main__':
    main()