import time
import copy

def main():
    path = "data.txt"
    # path = "test-data.txt"

    data = []
    start_time = time.perf_counter()
    with open(path) as f:
        rows = f.read().splitlines()
        p1 = int(rows[0][0])
        p2 = int(rows[0][1])
    
    # test()

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
    print(ans2)
    print(444356092776315 + 341960390180808)

def test():
    arr = [1,2,3]
    counts = {}
    for v1 in arr:
        for v2 in arr:
            for v3 in arr:
                s = v1 + v2 + v3
                if s not in counts:
                    counts[s] = 1
                    continue
                counts[s] += 1
    for key, val in counts.items():
        print(key, val)
    exit()

def star1(p1, p2):
    rollCount = 0
    dice = 0
    s1 = 0
    s2 = 0
    while s1 < 1000 and s2 < 1000:
        dice, rollCount, s = rollDice(dice, rollCount, 3)
        p1 = (p1 + s - 1) % 10 + 1
        s1 += p1
        if s1 >= 1000:
            break
        dice, rollCount, s = rollDice(dice, rollCount, 3)
        p2 = (p2 + s - 1) % 10 + 1
        s2 += p2
    loser = min(s1, s2)
    return loser * rollCount

def rollDice(dice, rollCount, n):
    s = 0
    for i in range(n):
        rollCount += 1
        dice += 1
        if dice > 100:
            dice = 1
        s += dice
    return dice, rollCount, s

def star2(p1, p2):
    outcomes1 = {}
    outcomes2 = {}
    outcomes1[(0, p1)] = 1
    outcomes2[(0, p2)] = 1
    N = 11
    won1 = 0
    won2 = 0
    univ1 = 1
    univ2 = 1
    for i in range(N):
        outcomes1 = diraqStep(outcomes1)
        univ1 *= 27
        newOutcomes1 = copy.deepcopy(outcomes1)
        newWon1 = 0
        newLen = 0
        for key, val in outcomes1.items():
            newLen += val
        if univ1 == newLen:
            print(i, univ1)
        for key, val in outcomes1.items():
            if key[0] >= 21:
                newWon1 += val
                del newOutcomes1[key]
        # for key, val in outcomes1.items():
        #     print(key, val)
        # print('----')
        won1 += newWon1 * univ2
        univ1 -= newWon1
        outcomes1 = newOutcomes1
        outcomes2 = diraqStep(outcomes2)
        univ2 *= 27
        newOutcomes2 = copy.deepcopy(outcomes2)
        newWon2 = 0
        for key, val in outcomes2.items():
            if key[0] >= 21:
                newWon2 += val
                del newOutcomes2[key]
        won2 += newWon2 * univ1
        univ2 -= newWon2
        outcomes2 = newOutcomes2
    outcomes1 = newOutcomes1
    for key, val in outcomes1.items():
        print(key, val)
    print('----')
    for key, val in outcomes2.items():
        print(key, val)
    print(won1)
    print(won2)
    return won1 + won2

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