import time

def main():
    path = "data.txt"
    seq = []
    inst = {}
    counts = {}
    cache_empty = {}
    for row in open(path, 'r').read().splitlines():
        if not seq:
            seq = row
            continue
        if row:
            r = row.split(' -> ')
            inst[(r[0][0], r[0][1])] = r[1]
            cache_empty[(r[0][0], r[0][1])] = 0
            counts[r[0][0]] = 0 
            counts[r[0][1]] = 0 
    start_time = time.time()
    c = cache_empty.copy()
    for i in range(len(seq) -1):
        c[(seq[i], seq[i+1])] += 1
    N = 40
    counts[seq[-1]] = 1
    for i in range(N):
        new_c = cache_empty.copy()
        for sub in c:
            new_c[(sub[0], inst[sub])] += c[sub]
            new_c[(inst[sub], sub[1])] += c[sub]
        c = new_c
    for sub in c:
        counts[sub[0]] += c[sub]
    d = print_max_min(counts)
    dt = time.time() - start_time
    print(dt)
    print(d)

def print_max_min(counts):
    ma = counts[max(counts, key=counts.get)]
    mi = counts[min(counts, key=counts.get)]
    return (ma - mi)

if __name__ == '__main__':
    main()