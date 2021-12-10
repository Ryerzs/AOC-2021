import time

def main():
    path = "data.txt"
    data = [row for row in open(path, 'r').read().splitlines()]
    start_time = time.time()

    brackets = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
    opened = [p[0] for p in brackets]

    incomplete, ans1 = star1(data, brackets)
    ans2 = star2(incomplete, opened)

    dt = time.time() - start_time
    print(dt)
    print("Star 1:", ans1)
    print("Star 2:", ans2)

def star1(data, brackets):
    op_br = [p[0] for p in brackets]
    cl_br = [p[1] for p in brackets]
    corrupt = [0]*4
    incomplete = []
    for i in range(len(data)):    
        opened = []
        corrupted = False
        for c in data[i]:
            if len(opened) < 1:
                opened.append(c)
                continue
            c1 = opened[-1]
            if not open_close_brackets(c1, c, op_br, cl_br):
                opened.append(c)
                continue
            if brackets_match(c1, c, brackets):
                opened.pop(-1)
            else:
                corrupted = True
                i = cl_br.index(c)
                corrupt[i] += 1
                break
        if not corrupted:
            incomplete.append(opened)
    val = [3, 57, 1197, 25137]
    return incomplete, sum([corrupt[i] * val[i] for i in range(4)])

def open_close_brackets(c1, c2, op_br, cl_br):
    return c1 in op_br and c2 in cl_br

def brackets_match(c1, c2, brackets):
    return sum([c1==p[0] and c2==p[1] for p in brackets])

def star2(data, op_br):
    scores = []
    for row in data:
        score = 0
        l = len(row)
        for i in range(l):
            score *= 5
            score += op_br.index(row[l-i-1])+1
        scores.append(score)
    if scores == []:
        return 0
    scores.sort()
    i_mid = len(scores)//2
    return scores[i_mid]

if __name__ == '__main__':
    main()