import time
import numpy as np
from collections import defaultdict, Counter, deque

def main():
    path = "data.txt"
    path = "test-data.txt"
    seq = []
    inst = {}
    counts = {}
    dict_counter = 0
    lett_dict = {}
    for row in open(path, 'r').read().splitlines():
        if not seq:
            for c in row:
                if c not in lett_dict:
                    lett_dict[c] = dict_counter
                    dict_counter += 1
                seq.append(lett_dict[c])
            continue
        if row:
            r = row.split(' -> ')
            c1 = r[0][0]
            c2 = r[0][1]
            c3 = r[1]
            if c1 not in lett_dict:
                lett_dict[c1] = dict_counter
                dict_counter += 1
            if c2 not in lett_dict:
                lett_dict[c2] = dict_counter
                dict_counter += 1
            if c3 not in lett_dict:
                lett_dict[c3] = dict_counter
                dict_counter += 1
            i1 = lett_dict[c1]
            i2 = lett_dict[c2]
            i3 = lett_dict[c3]
            inst[(i1, i2)] = i3
            
            if i3 not in counts:
                counts[i3] = 0
    start_time = time.time()
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
    print(counts)
    ma = counts[max(counts, key=counts.get)]
    mi = counts[min(counts, key=counts.get)]
    print(ma, mi)
    print(ma - mi)

    dt = time.time() - start_time
    print(dt)

if __name__ == '__main__':
    main()