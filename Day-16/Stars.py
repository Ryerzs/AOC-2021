import time

def main():
    path = "data.txt"
    start_time = time.time()
    data = [bin(int(row, 16))[2:].zfill(len(row)*4) for row in 
                open(path, 'r').read().splitlines()]

    inp = data[0]
    num, version_sum, _ = unravel_inp(inp)
    if not type(num) == int:
        return False

    dt = time.time() - start_time
    print(num)
    print(version_sum)
    print(dt)

def literal(inp_str):
    last = False
    packets = ''
    ind = 6
    while not last:
        if inp_str[ind] == '0':
            last = True
        packet = inp_str[ind+1:ind+5]
        packets = packets + packet
        ind += 5
    num = int(packets, 2)
    return num, ind

def unravel_inp(inp_str):
    num = []
    version_sum = int(inp_str[0:3], 2)
    type_id = int(inp_str[3:6], 2)
    if type_id == 4:
        num, tot_len = literal(inp_str)
        return num, version_sum, tot_len

    length_id = int(inp_str[6:7])
    if length_id == 0:
        cond = condition1
    else:
        cond = condition2

    inp_str = inp_str[7:]
    length_type = 15 - 4*length_id
    rest = inp_str[length_type:]
    length = int(inp_str[0:length_type], 2)
    cur_len = 0
    i = 0
    while cond(cur_len, length, i):
        n, v, l = unravel_inp(rest)
        num.append(n)
        version_sum += v
        cur_len += l
        rest = rest[l:]
        i += 1
    num = perform_operation(num, type_id)
    tot_len = 7 + length_type + cur_len
    return num, version_sum, tot_len

def condition1(cur_len, length, i):
    return cur_len != length

def condition2(cur_len, length, i):
    return i < length

def perform_operation(num, op):
    s = 1
    if op == 0:
        s = sum(num)
    elif op == 1:
        for n in num:
            s *= n
    elif op == 2:
        s = min(num)
    elif op == 3:
        s = max(num)
    elif op == 5:
        s = int(num[0] > num[1])
    elif op == 6:
        s = int(num[0] < num[1])
    elif op == 7:
        s = int(num[0] == num[1])
    return s

if __name__ == '__main__':
    main()