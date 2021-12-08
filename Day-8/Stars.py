import time
import numpy as np

def main():
    path = "data.txt"
    data = [[[s for s in data_type.split(" ")] for data_type in row.split(" | ")]
                for row in open(path, 'r').read().splitlines()]
    start_time = time.time()
    N = 100
    for i in range(N):
        data_test = [data[i][0] for i in range(len(data))]
        data_out  = [data[i][1] for i in range(len(data))]
        ans1 = star1(data_out)
        ans2 = star2(data_test, data_out)
    dt = (time.time() - start_time)/N
    print("Star 1:", ans1)
    print("Star 2:", ans2)
    print(dt) # Takes roughly 3.8 ms

def star1(data):
    count = sum([sum([1 for el in row
                if len(el) == 2 or len(el) == 3 or len(el) == 4 or len(el) == 7])
                for row in data])
    return count

def star2(data_test, data_out):
    total = 0
    for i in range(len(data_test)):
        d_t = [set(el) for el in data_test[i]]
        d_o = [set(el) for el in data_out[i]]
        num = [""]*10
        num[1] = find_general(d_t, cond_one, None)
        num[4] = find_general(d_t, cond_four, None)
        num[7] = find_general(d_t, cond_seven, None)
        num[8] = find_general(d_t, cond_eight, None)
        num[6] = find_general(d_t, cond_six, num[7])
        num[9] = find_general(d_t, cond_nine, num[4])
        num[3] = find_general(d_t, cond_three, num[7])
        num[5] = find_general(d_t, cond_five, num[6])
        num[0] = find_general(d_t, cond_zero, None)
        num[2] = d_t[0]
        total += get_output(d_o, num)
    return total

def get_output(data, num):
    number = ""
    for el in data:
        # Concat index that element is at in number list
        number += str(num.index(el))
    return int(number)

def cond_zero(a, _):
    return len(a) == 6

def cond_one(a, _):
    return len(a) == 2

def cond_three(a, seven):
    return len(a & seven) == 3 and len(a) == 5

def cond_four(a, _):
    return len(a) == 4

def cond_five(a, six):
    return len(a & six) == 5 and len(a) == 5

def cond_six(a, seven):
    return len(a & seven) == 2 and len(a) == 6

def cond_seven(a, _):
    return len(a) == 3

def cond_eight(a, _):
    return len(a) == 7

def cond_nine(a, four):
    return len(a & four) == 4 and len(a) == 6

def find_general(data, func, par):
    for el in data:
        if func(el, par):
            data.remove(el)
            return el

if __name__ == '__main__':
    main()