import time

def main():
    path = "Day-3/data.txt"
    # path = "Day-3/data.txt"
    lines = [[int(el) for el in row] for row in open(path, "r",encoding="utf-8").read().splitlines()]
    row = len(lines[0])
    start_time = time.time()

    set_g = find_set(lines, bigger_than_eq)
    set_e = find_set(lines, less_than)
    gamma = sum([set_g[0][-i-1]*2**(i) for i in range(row)])
    epsilon = sum([set_e[0][-i-1]*2**(i) for i in range(row)])

    dt = time.time() - start_time
    print(dt)
    print(gamma * epsilon)

def find_set(base_list, func):
    row = len(base_list[0])
    set_left = base_list
    for i in range(row):
        common = [int(func(sum(el[i] for el in set_left),len(set_left)/2))]
        indeces = [j for j in range(len(set_left)) if common[0] == int(set_left[j][i])]
        set_left = [set_left[j] for j in indeces]
        if len(set_left) <= 1:
            return(set_left)
    return []

def less_than(a,b):
    return(a<b)

def bigger_than_eq(a,b):
    return(a>=b)

if __name__ == '__main__':
    main()