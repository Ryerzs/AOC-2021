import time

def main():
    path = "data.txt"
    start_time = time.time()
    data = [bin(int(row, 16))[2:].zfill(len(row)*4) for row in 
                open(path, 'r').read().splitlines()]

    inp = data[0]
    unraveled, ver, _ = unravel_inp(inp)
    if type(unraveled) == int:
        num = unraveled

    dt = time.time() - start_time
    print(num)
    print(ver)
    print(dt)

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
    num = []
    header = int(inp[0:3], 2)
    ver = header
    type_id = int(inp[3:6], 2)
    if type_id == 4:
        num, l = literal(inp)
        return num, ver, l
    length_id = int(inp[6:7])
    if length_id == 0:
        # The length bits is 15 bits
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
        num = perform_operation(num, type_id)
        tot_len = 22 + cur_len
    else:
        # The length bits is 11 bits
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
        num = perform_operation(num, type_id)
        tot_len = 18 + cur_len
    return num, ver, tot_len

def perform_operation(num, op):
    s = 0
    if op == 0:
        for n in num:
            s += n
    elif op == 1:
        s = 1
        for n in num:
            s *= n
    elif op == 2:
        s = num[0]
        for n in num:
            if n < s:
                s = n
    elif op == 3:
        s = num[0]
        for n in num:
            if n > s:
                s = n
    elif op == 5:
        n1 = num[0]
        n2 = num[1]
        s = int(n1 > n2)
    elif op == 6:
        n1 = num[0]
        n2 = num[1]
        s = int(n1 < n2)
    elif op == 7:
        n1 = num[0]
        n2 = num[1]
        s = int(n1 == n2)
    return s

if __name__ == '__main__':
    main()