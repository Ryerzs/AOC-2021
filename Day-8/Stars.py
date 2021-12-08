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
        num[1] = find_one(d_t)
        num[4] = find_four(d_t)
        num[7] = find_seven(d_t)
        num[8] = find_eight(d_t)
        num[6] = find_six(d_t, num[7])
        num[9] = find_nine(d_t, num[4])
        num[3] = find_three(d_t, num[7])
        num[5] = find_five(d_t, num[6])
        num[0] = find_zero(d_t)
        num[2] = d_t[0]
        total += get_output(d_o, num)
    return total

def get_output(data, num):
    number = ""
    for el in data:
        # Concat index that element is at in number list
        number += str(num.index(el))
    return int(number)

def find_zero(data):
    for el in data:
        if len(el) == 6:
            data.remove(el) 
            return el

def find_one(data):
    for el in data:
        if len(el) == 2:
            data.remove(el) 
            return el

def find_three(data, seven):
    for el in data:
        if len(el & seven) == 3 and len(el) == 5:
            data.remove(el) 
            return el

def find_four(data):
    for el in data:
        if len(el) == 4:
            data.remove(el) 
            return el

def find_five(data, six):
    for el in data:
        if len(el & six) == 5 and len(el) == 5:
            data.remove(el) 
            return el

def find_six(data, seven):
    for el in data:
        if len(el & seven) == 2 and len(el) == 6:
            data.remove(el) 
            return el

def find_seven(data):
    for el in data:
        if len(el) == 3:
            data.remove(el) 
            return el

def find_eight(data):
    for el in data:
        if len(el) == 7:
            data.remove(el) 
            return el

def find_nine(data, four):
    for el in data:
        if len(el & four) == 4 and len(el) == 6:
            data.remove(el) 
            return el

if __name__ == '__main__':
    main()