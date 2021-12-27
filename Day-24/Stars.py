import time
from Instruction import *

def main():
    path = "data.txt"
    # path = "test-data.txt"


    data = []
    start_time = time.perf_counter()
    data = getData(path)
    inputNumber = deque([])
    number = '17153114691118'
    for i in range(14):
        inputNumber.append(int(number[i]))
    w1 = int(number[0])
    w2 = int(number[1])
    w3 = int(number[2])
    w4 = int(number[3])
    w5 = int(number[4])
    w6 = int(number[5])
    w7 = int(number[6])
    w8 = int(number[7])
    w9 = int(number[8])
    w10 = int(number[9])
    w11 = int(number[10])
    w12 = int(number[11])
    w13 = int(number[12])
    w14 = int(number[13])
    variables = {}
    variables['x'] = 0
    variables['y'] = 0
    variables['z'] = 0
    variables['w'] = 0
    for inst in data:
        inst.setInput(inputNumber)
        inst.setVariables(variables)
    # test(data)

    time1 = time.perf_counter()
    y1 = w1 + 7
    y2 = w2 + 4
    y5 = w5 + 5
    y6 = w6 + 14
    y7 = w7 + 12
    y8 = 0
    y9 = 0
    y10 = w10 + 7
    y11 = 0
    y12 = 0
    y13 = 0
    z13 = y1
    print(y13, z13)

    ans1 = star1(data, 14)
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

def test():
    s = '-1'
    numberTail = '1'*11
    exit()

def getData(path):
    with open(path) as f:
        rows = f.read().splitlines()
        instructions = []
        for r in rows:
            rawInst = r.split(' ')
            instructions.append(getInst(rawInst))
    return instructions

def getInst(inst):
    newInst = Instruction()
    newInst.type = inst[0]
    newInst.var = inst[1]
    if inst[0] != 'inp':
        newInst.val = inst[2]
    return newInst

def star1(data, N):
    print(data[0].variables)
    i = 0
    for inst in data:
        if inst.type == 'inp':
            i += 1
        if i <= N:
            inst.performInstruction()
    print(data[0].variables)
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()
