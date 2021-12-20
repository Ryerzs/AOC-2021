import time
import numpy as np
from collections import Counter

def main():
    path = "data.txt"
    path = "test-data1.txt"
    # path = "test-data.txt"
    # path = "test-data2.txt"

    start_time = time.perf_counter()
    data = getData(path)

    # test(data)

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2(data)
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

def test(data):
    a = np.array([[1,2],[3,4]])
    b = np.array([2,1])
    print(a + b)
    exit()

def matSort(mat, col:int = 0, variant:int = 0, s:int = 2):
    m = mat.copy()
    mSort = []
    for i in range(s+1):
        if variant:
            c = (col - i - 1)%(s+1)
        else:
            c = (col + i + 1)%(s+1)
        mSort.append(m[:,c])
    m = m[np.lexsort(mSort)]
    return m


def getData(path):
    with open(path) as f:
        rows = f.read().splitlines()
        data = extractRowInfo(rows)
    return data

def extractRowInfo(rows):
    Sensors = []
    currentSensor = -1
    beaconPoints = []
    for row in rows:
        if row == '':
            continue
        if row[0:2] == '--':
            currentSensor += 1
            appendIfNotEmpty(Sensors, beaconPoints)
            continue
        beaconPoints.append(stringPointToIntPoint(row))
    appendIfNotEmpty(Sensors, beaconPoints)
    return Sensors

def appendIfNotEmpty(list, listAppend):
    if listAppend != []:
        list.append(np.array(listAppend))
    listAppend.clear()

def stringPointToIntPoint(string):
    return [int(sv) for sv in string.split(',')]


def star1(data):
    relativeScannerDist = {}
    trans = getAllTransformations()
    transInv = inv(trans)
    base0 = {}
    for i in range(len(data)):
        base0[i] = False
    base0[0] = True
    base = data[0]
    otherSensors = data[1:]
    while otherSensors:
        base, otherSensors = findNextBase(base, otherSensors, trans, transInv)
    print(len(base))
    beacons = findAllBeacons(base)
    print(len(beacons))
    return 0

def findNextBase(base, otherSensors, trans, transInv):
    dTrans = transformMatrix(base, trans)
    relativePositions = []
    for k, dv in enumerate(otherSensors):
        relative = isRelativeTo(dTrans, dv, transInv, k)
        if relative != []:
            base, otherSensors = mergeToBase(base, otherSensors, transInv, k, relative)
            break
    return base, otherSensors

def mergeToBase(base, otherSensors, transInv, k, rel):
    off = rel[0]
    t = rel[1]
    other = np.matmul(otherSensors[k], transInv[t]) + off
    base = np.concatenate((base, other))
    otherSensors = otherSensors[:k] + otherSensors[k+1:]
    return base, otherSensors

def isRelativeTo(dTrans, dv, transInv, k):
    for i, dT in enumerate(dTrans):
        relativePos = getRelativePositions(dT, dv, transInv, i, k)
        if relativePos != []:
            return relativePos
    return []

def findAllBeacons(data):
    beacons = {}
    for i, d in enumerate(data):
        coord = tuple(d)
        beacons[coord] = 1
    return beacons

def transformData(rel, data, transInv, j, base0):
    for r in rel:
        ind = r[2]
        t = r[1]
        if not base0[ind]:
            data[ind] = np.matmul(data[ind], transInv[t])
        base0[ind] = True
    return rel, data, base0


def useRelative(ar, cur, i, pointsTo):
    for r in cur:
        ind = r[2]
        if pointsTo[ind] == []:
            pointsTo[ind] = r[0] + pointsTo[i]
            useRelative(ar, ar[ind], ind, pointsTo)
    # for i, rel in enumerate(ar):
    #     pointsToIndex = []
    #     for r in rel:
    #         pointsToIndex.append((r[0], r[1], r[2]))
    #     pointsTo[i] = pointsToIndex
    # for key, val in pointsTo.items():
    #     print(key, val)

def transformMatrix(d, trans):
    dTrans = []
    for T in trans:
        dTrans.append(np.matmul(d, T))
    return dTrans

def getRelativePositions(dT, dv, transInv, i, k):
    relativePositions = []
    relativeDistances = {}
    for p1 in dT:
        for p2 in dv:
            diff = tuple(p1 - p2)
            if diff not in relativeDistances:
                relativeDistances[diff] = 1
                continue
            relativeDistances[diff] += 1
            if relativeDistances[diff] == 12:
                orig = np.array(diff, dtype=int)
                orig = np.matmul(diff, transInv[i])
                # relativePositions.append([orig, relativeDistances[diff], k])
                relativePositions = [orig, i, k]
                break
    return relativePositions

def inv(trans:'list'):
    inverses = []
    for T in trans:
        inverses.append(np.linalg.inv(T).astype(int))
    return inverses

def getAllTransformations():
    I = np.eye(3, dtype=int)
    # Rotates matrix along xy plane, positive mathematical orientation
    Axy = np.array([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ])
    Ayz = np.array([
        [1, 0, 0],
        [0, 0, 1],
        [0, -1, 0]
    ])
    Axz = np.array([
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0]
    ])
    transformations = []
    xyTrans = []
    zTrans  = []
    Axy2 = np.matmul(Axy, Axy)
    Axy3 = np.matmul(Axy2, Axy)
    xyTrans.append(I)
    xyTrans.append(Axy)
    xyTrans.append(Axy2)
    xyTrans.append(Axy3)
    Ayz2 = np.matmul(Ayz, Ayz)
    Ayz3 = np.matmul(Ayz2, Ayz)

    zTrans.append(I)
    zTrans.append(Ayz)
    zTrans.append(Ayz2)
    zTrans.append(Ayz3)
    Axz2 = np.matmul(Axz, Axz)
    Axz3 = np.matmul(Axz2, Axz)
    zTrans.append(Axz)
    zTrans.append(Axz3)
    for z in zTrans:
        for xy in xyTrans:
            transformations.append(np.matmul(z, xy))
    return transformations



def star2(data):
    return 0

if __name__ == '__main__':
    main()