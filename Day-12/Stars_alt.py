import time
import numpy as np
from Node import *

def main():
    path = "data.txt"
    # path = "test-data3.txt"
    data_in = [[el for el in row.split("-")] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()

    fro = [row[0] for row in data_in]
    to = [row[1] for row in data_in]
    all_nodes = set(fro) | set(to)
    temp = all_nodes.difference({'start', 'end'})
    small = []
    for n in temp:
        if n.lower() == n:
            small.append(n)
    big = temp.difference(small)
    nodes = []
    dic = {}
    nodes.append(Node('start', False, 0))
    l1 = len(small)
    dic["start"] = []
    l2 = len(big)
    for i in range(l1):
        nodes.append(Node(small[i], False, 1 + i))
        dic[small[i]] = []
    i = 0
    for n in big:
        nodes.append(Node(n, True, 1 + l1 + i))
        dic[n] = []
        i+=1
    nodes.append(Node('end', False, 1 + l1 + l2))
    dic["end"] = []
    new_ord = [[None, None] for i in range(len(data_in))]
    for i in range(len(data_in)):
        for j in range(len(nodes)):
            if data_in[i][0] == nodes[j].name:
                new_ord[i][0] = j
        for j in range(len(nodes)):
            if data_in[i][1] == nodes[j].name:
                new_ord[i][1] = j
    for p in new_ord:
        if nodes[p[1]].name != 'start' and nodes[p[0]].name != 'end':
            dic[nodes[p[0]].name].append(nodes[p[1]].name)
        if nodes[p[0]].name != 'start' and nodes[p[1]].name != 'end':
            dic[nodes[p[1]].name].append(nodes[p[0]].name)
    ans2 = 0

    path = ['start']
    counts = {}
    for d in dic:
        counts[d] = 0
    ans2 = find_paths(path, dic, counts, None)

    dt2 = time.time() - start_time
    print("Star 2:", ans2, "| Time:", dt2)

def find_paths(path, dic, counts, p_double):
    tot = 0
    cur = path[-1]
    if cur == 'end':
        return 1
    if counts[cur] == 1:
        if cur.lower() == cur:
            if not p_double == None and not cur == p_double:
                return 0
            p_double = cur
    elif counts[cur] > 1:
        if cur.lower() == cur:
            return 0
    counts[cur] += 1
    for p in dic[cur]:
        path.append(p)
        tot += find_paths(path, dic, counts, p_double)
        path.pop()
    counts[cur] -= 1
    
    return tot

if __name__ == '__main__':
    main()
