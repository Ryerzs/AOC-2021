import time
import numpy as np
from collections import defaultdict, Counter, deque

def main():
    path = "data.txt"
    path = "test-data.txt"
    seq = ""
    inst = {}
    counts = {}
    for row in open(path, 'r').read().splitlines():
        if not seq:
            seq = row
            continue
        if row:
            r = row.split(' -> ')
            inst[(r[0][0], r[0][1])] = r[1]
            if r[1] not in counts:
                counts[r[1]] = 0
    inst[seq[0]] = ""
    start_time = time.time()
    N = 1
    Q = deque([])
    for i in range(len(seq) -1):
        Q.append((seq[i], seq[i+1]))
    last = seq[-1]
    l = len(seq)
    N = 20
    p = 2**N
    for i in range((p-1)*l - p):
        sub = Q.popleft()
        Q.append((sub[0], inst[sub]))
        Q.append((inst[sub], sub[1]))
    for sub in Q:
        counts[sub[0]] += 1
    counts[last] += 1
    # comp = ''.join(done)
    # print(comp)
    # for i in range(0, N):
    #     # prev = seq[0]
    #     new_seq = [seq[0]]
        
    #     for i in range(len(seq) - 1):
    #         # new_seq = f'{new_seq}{inst[prev+c]}'
    #         print(seq[i:i+2])
    #         new_seq.append(inst[seq[i:i+2]])
    #         new_seq.append(seq[i+1])
    #         # new_seq = new_seq + inst[prev+c] + c
    #         # new_seq = new_seq + inst[prev+c]
    #         # new_seq = new_seq + c
    #         if i == N - 1:
    #             dict_add(counts, inst[seq[i:i+2]], 1)
    #             dict_add(counts, seq[i+1], 1)
    #     seq = ''.join(new_seq)

    

    # for c in comp:
    #     if c in counts:
    #         counts[c] += 1
    #         continue
    #     counts[c] = 1
    # print(seq)
    print(inst)
    # if '' in counts:
    #     counts.pop('')
    print(counts)
    ma = counts[max(counts, key=counts.get)]
    mi = counts[min(counts, key=counts.get)]
    print(ma, mi)
    print(ma - mi)

    ans1 = star1()
    ans2 = star2()

    dt = time.time() - start_time
    print(dt)
    print("Star 1:", ans1)
    print("Star 2:", ans2)

def dict_add(dic, n, a):
    if n in dic:
        dic[n] += a
        return
    dic[n] = a

def star1():
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()