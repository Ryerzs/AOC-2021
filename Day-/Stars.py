import time

def main():
    path = "data.txt"
    path = "test-data.txt"

    data = []
    start_time = time.perf_counter()
    with open(path) as f:
        rows = f.read().splitlines()
        for r in rows:
            print(r)

    time1 = time.perf_counter()

    ans1 = star1(data)
    time2 = time.perf_counter()

    ans2 = star2()
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

def star1():
    return 0

def star2():
    return 0

if __name__ == '__main__':
    main()