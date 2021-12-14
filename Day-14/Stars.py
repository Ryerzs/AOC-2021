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
    
    N = 20
    seq_1 = Q.popleft()
    last = seq_1[-1]
    cache = {}
    count_1 = counts.copy()
    if seq_1 in cache:
        c = cache[seq_1][0]
    else:
        depth_search(seq_1, inst, count_1, 0, 1)


    dt = time.time() - start_time
    print(dt)
    return
    for seq_1 in Q:
        depth_search(seq_1, inst, counts, 0, N)
        counts[seq_1[1]] += 1
    print_max_min(counts)
    dt = time.time() - start_time
    print(dt)
    return
    # last = seq[-1]
    # l = len(seq)
    # N = 20
    # p = 2**N
    # for i in range((p-1)*l - p):
    #     sub = Q.popleft()
    #     Q.append((sub[0], inst[sub]))
    #     Q.append((inst[sub], sub[1]))
    # for sub in Q:
    #     counts[sub[0]] += 1
    # counts[last] += 1
    # print(counts)
    # ma = counts[max(counts, key=counts.get)]
    # mi = counts[min(counts, key=counts.get)]
    # print(ma, mi)
    # print(ma - mi)

    # dt = time.time() - start_time
    # print(dt)

def depth_search(seq, inst, counts, depth, N):
    if depth == N:
        counts[seq[0]] += 1
        return
    depth_search((seq[0], inst[seq]), inst, counts, depth + 1, N)
    depth_search((inst[seq], seq[1]), inst, counts, depth + 1, N)
    return

def print_max_min(counts):
    ma = counts[max(counts, key=counts.get)]
    mi = counts[min(counts, key=counts.get)]
    print(ma, mi)
    print(ma - mi)
    return (ma - mi)

if __name__ == '__main__':
    main()