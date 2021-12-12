import time
import numpy as np
from Node import *

def main():
    path = "data.txt"
    data_in = [[el for el in row.split("-")] for row in open(path, 'r').read().splitlines()]
    start_time = time.time()

    ans1, nodes = star1(data_in)
    dt1 = time.time() - start_time
    ans2 = star2(nodes)

    dt2 = time.time() - start_time - dt1
    print("Star 1:", ans1, "| Time:", dt1)
    print("Star 2:", ans2, "| Time:", dt2)

def star1(data_in):
    # print(data_in)
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
    nodes.append(Node('start', False, 0))
    l1 = len(small)
    l2 = len(big)
    for i in range(l1):
        nodes.append(Node(small[i], False, 1 + i))
    i = 0
    for n in big:
        nodes.append(Node(n, True, 1 + l1 + i))
        i+=1
    nodes.append(Node('end', False, 1 + l1 + l2))
    new_ord = [[None, None] for i in range(len(data_in))]
    for i in range(len(data_in)):
        for j in range(len(nodes)):
            if data_in[i][0] == nodes[j].name:
                new_ord[i][0] = j
        for j in range(len(nodes)):
            if data_in[i][1] == nodes[j].name:
                new_ord[i][1] = j
    for p in new_ord:
        nodes[p[0]].add_neighbor(nodes[p[1]])
    for n in nodes:
        n.set_ref_to_all(nodes)
    #     print(n.name, " and neigh: ", n.get_neigh_names())
    
    tot = nodes[0].find_path([])

    return tot, nodes

def star2(nodes):
    for n in nodes:
        n.passed = 0

    tot = nodes[0].find_path_2([])
    return tot

if __name__ == '__main__':
    main()
