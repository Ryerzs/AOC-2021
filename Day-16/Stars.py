import time
import numpy as np

def main():
    path = "data.txt"
    # path = "test-data1.txt"
    # path = "test-data2.txt"
    data = [bin(int(row, 16))[2:].zfill(len(row)*4) for row in 
                open(path, 'r').read().splitlines()]
    start_time = time.time()

    num = []
    oper = []
    ver = []
    for inp in data:
        unraveled, v, _ = unravel_inp(inp)
        ver.append(v)
        if type(unraveled) == int:
            num.append(unraveled)
            continue
        for u in unraveled:
            if type(u) == int:
                num.append(u)

    print(num)
    print(ver)

    ans1 = star1()
    ans2 = star2()

    dt = time.time() - start_time
    print(dt)
    print("Star 1:", ans1)
    print("Star 2:", ans2)

def literal(inp):
    last = False
    packets = ''
    ind = 6
    while not last:
        if inp[ind] == '0':
            last = True
        packet = inp[ind+1:ind+5]
        packets = packets + packet
        ind += 5
    num = int(packets, 2)
    return num, ind

def unravel_inp(inp):
    oper = []
    num = []
    header = int(inp[0:3], 2)
    ver = header
    type_id = int(inp[3:6], 2)
    print(header, type_id)
    if type_id == 4:
        num, l = literal(inp)
        return num, ver, l
    length_id = int(inp[6:7])
    print(length_id)
    if length_id == 0:
        # The length bits are 15 bits
        cur_len = 0
        length = int(inp[7:22], 2)
        rest = inp[22:]
        while cur_len != length:
            unraveled, v, l = unravel_inp(rest)
            ver += v
            if type(unraveled) == int:
                num.append(unraveled)
            cur_len += l
            rest = rest[l:]
        tot_len = 22 + cur_len
    else:
        length = int(inp[7:18], 2)
        rest = inp[18:]
        cur_len = 0
        for i in range(length):
            unraveled, v, l = unravel_inp(rest)
            cur_len += l
            if type(unraveled) == int:
                num.append(unraveled)
            ver += v
            rest = rest[l:]
        tot_len = 18 + cur_len
    return num, ver, tot_len


def star1():
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()