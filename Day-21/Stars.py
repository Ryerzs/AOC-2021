import time
import copy
from collections import deque

def main():
    path = "data.txt"
    # path = "test-data.txt"

    data = []
    start_time = time.perf_counter()
    with open(path) as f:
        rows = f.read().splitlines()
        p1 = int(rows[0][0])
        p2 = int(rows[0][1])

    time1 = time.perf_counter()

    ans1 = star1(p1, p2)
    time2 = time.perf_counter()

    ans2 = star2(p1, p2)
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

def star1(p1, p2):
    rollCount = 0
    dice = 0
    players = deque([])
    players.append([p1, 0])
    players.append([p2, 0])
    while players:
        p = players.popleft()
        dice, rollCount, s = rollDice(dice, rollCount, 3)
        p[0] = (p[0] + s - 1) % 10 + 1
        p[1] += p[0]
        if p[1] < 1000:
            players.append(p)
            continue
        loser = players.popleft()
    return loser[1] * rollCount

def rollDice(dice, rollCount, n):
    s = 0
    rollCount += n
    for i in range(n):
        dice = dice % 100 + 1
        s += dice
    return dice, rollCount, s

def star2(p1, p2):
    outcomes1 = {}
    outcomes2 = {}
    outcomes1[(0, p1)] = 1
    outcomes2[(0, p2)] = 1
    N = 30
    won1 = 0
    won2 = 0
    univ1 = 1
    univ2 = 1
    players = deque([])
    players.append([outcomes1, univ1, won1])
    players.append([outcomes2, univ2, won2])
    prevUniv = 1
    for i in range(N):
        p = players.popleft()
        universeSplit(p, prevUniv)
        prevUniv = p[1]
        players.append(p)

    return max(players[0][2], players[1][2])

def universeSplit(p, univ2):
    p[0] = diraqStep(p[0])
    p[1] *= 27
    newOutcomes = copy.deepcopy(p[0])
    newWon = 0
    for key, val in p[0].items():
        if key[0] >= 21:
            newWon += val
            del newOutcomes[key]
    p[2] += newWon * univ2
    p[1] -= newWon
    p[0] = newOutcomes
    

def diraqStep(outcomes):
    poss = {}
    poss[3] = 1
    poss[4] = 3
    poss[5] = 6
    poss[6] = 7
    poss[7] = 6
    poss[8] = 3
    poss[9] = 1
    newOutcomes = {}
    for key1, val1 in outcomes.items():
        for key2, val2 in poss.items():
            p = (key1[1] + key2 - 1)%10 +1
            s = key1[0] + p
            if (s, p) not in newOutcomes:
                newOutcomes[(s, p)] = val1*val2
                continue
            old = newOutcomes[(s, p)]
            newOutcomes[(s, p)] = old + val1*val2
    return newOutcomes

if __name__ == '__main__':
    main()