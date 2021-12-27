import time

def main():
    path = "data.txt"
    # path = "test-data.txt"

    data = []
    start_time = time.perf_counter()
    size, data = getData(path)
    for key, value in data.items():
        print(key, value)

    time1 = time.perf_counter()

    ans1 = star1(data, size)
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

def getData(path):
    with open(path) as f:
        rows = f.read().splitlines()
        cucumbers = {}
        size = [len(rows), len(rows[0])]
        for j, r in enumerate(rows):
            for i, cv in enumerate(r):
                if cv == '>':
                    cucumbers[(i,j)] = 'E'
                if cv == 'v':
                    cucumbers[(i,j)] = 'S'
    return size, cucumbers

def star1(data, size):
    steps = 0
    printBoard(data, size)
    still = False
    while not still:
        still, data = performOneStep(data, size)
        steps += 1
    print('----')
    printBoard(data, size)
    print(f'It took {steps} steps!')
    return 0

def star2():
    return 0

def performOneStep(data, size):
    newCucumbers = {}
    for point, direc in data.items():
        if direc == 'S':
            newCucumbers[point] = direc
            continue
        coord = getNextCoord(point, direc, size)
        if coord not in data:
            newCucumbers[coord] = direc
            continue
        newCucumbers[point] = direc
    same = data == newCucumbers
    data = newCucumbers
    newCucumbers = {}
    for point, direc in data.items():
        if direc == 'E':
            newCucumbers[point] = direc
            continue
        coord = getNextCoord(point, direc, size)
        if coord not in data:
            newCucumbers[coord] = direc
            continue
        newCucumbers[point] = direc
    same = data == newCucumbers and same
    data = newCucumbers
    return same, newCucumbers

def getNextCoord(point, direc, size):
    newPoint = None
    if direc == 'E':
        newX = point[0] + 1
        if newX >= size[1]:
            newX = 0
        newPoint = (newX, point[1])
    if direc == 'S':
        newY = point[1] + 1
        if newY >= size[0]:
            newY = 0
        newPoint = (point[0], newY)
    return newPoint

def printBoard(data, size):
    grid = []
    for r in range(size[0]):
        row = []
        for j in range(size[1]):
            row.append(' ')
        grid.append(row)
    for key, val in data.items():
        char = '>' if val == 'E' else 'v'
        # print(key[1], key[0])
        grid[key[1]][key[0]] = char
    
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    main()