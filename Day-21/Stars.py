import time
import copy
from collections import deque

def main():
    path = "data.txt"

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
    players = deque([])
    players.append(createUniversePlayer(p1, 1, 0))
    players.append(createUniversePlayer(p2, 1, 0))
    N = 20
    prevUniverseSize = 1
    while 1:
        p = players.popleft()
        universeSplit(p, prevUniverseSize)
        prevUniverseSize = p[1]
        players.append(p)
        if not p[0]:
            break
    return max(players[0][2], players[1][2])

def universeSplit(p, otherUniverseSize):
    p[0] = diraqStep(p[0])
    p[1] *= 27
    newOutcomes = copy.deepcopy(p[0])
    wonUniverses = 0
    for key, val in p[0].items():
        if key[0] >= 21:
            wonUniverses += val
            del newOutcomes[key]
    p[2] += wonUniverses * otherUniverseSize
    p[1] -= wonUniverses
    p[0] = newOutcomes

def createUniversePlayer(p, universeSize, startSum):
    outcomes = {}
    outcomes[(0, p)] = 1
    return [outcomes, universeSize, startSum]

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
    for key, universes in outcomes.items():
        for newStep, occurunces in poss.items():
            prevSum = key[0]
            prevStep = key[1]
            step = (prevStep + newStep - 1)%10 +1
            s = prevSum + step
            sumStepPair = (s, step)
            if sumStepPair not in newOutcomes:
                newOutcomes[sumStepPair] = universes*occurunces
                continue
            oldValue = newOutcomes[sumStepPair]
            newOutcomes[sumStepPair] = oldValue + universes*occurunces
    return newOutcomes

if __name__ == '__main__':
    main()