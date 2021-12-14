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