import time
from Snail_Number import *

def main():
    path = "data.txt"
    # path = "test-data1.txt"
    data = []
    start_time = time.perf_counter()
    with open(path) as f:
        rows = f.read().splitlines()
        for r in rows:
            data.append(Snail_Number(split_to_array(r)))
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

def split_to_array(row):
    if row.isnumeric():
        return int(row)
    arr = [None, None]
    row = row[1:-1]
    open_indices = [pos for pos, val in enumerate(row) if val == '[']
    if not open_indices:
        splitted = row.split(',')
        for i, sv in enumerate(splitted):
            splitted[i] = sv.strip('[]')
        arr[0] = int(splitted[0])
        arr[1] = int(splitted[1])
        return arr

    first_bracket = min(open_indices)
    opened = 0
    for i, c in enumerate(row[first_bracket+1:]):
        if c == '[':
            opened += 1
        if c == ']':
            if not opened:
                first_bracket = (first_bracket, i + first_bracket + 1)
                break
            else:
                opened -= 1
    inside = row[first_bracket[0]:first_bracket[1] + 1]
    left = row[0:first_bracket[0]] + row[first_bracket[1]+1:]
    if left[0] == ',':
        arr[0] = split_to_array(inside)
        arr[1] = split_to_array(left[1:])
    else:
        arr[1] = split_to_array(inside)
        arr[0] = split_to_array(left[:-1])
    return arr

def star1(data):
    sn = []
    for sv in data:
        if sn == []:
            sn = sv
            continue
        sn = sn.add_snail(sv)
        sn.reduce()
    return sn.get_magnitude()

def star2(data):
    highest = 0
    for s1 in data:
        for s2 in data:
            sn = s1.add_snail(s2)
            sn.reduce()
            magnitude = sn.get_magnitude()
            highest = max(magnitude, highest)
    return highest

if __name__ == '__main__':
    main()