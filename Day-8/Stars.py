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
    print(dt) # Takes roughly 15.2 ms

def star1(data):
    count = sum([sum([1 for el in row
                if len(el) == 2 or len(el) == 3 or len(el) == 4 or len(el) == 7])
                for row in data])
    return count

def star2(data_test, data_out):
    total = 0
    for i in range(len(data_test)):
        # Sort data alphabetically
        d_t = ["".join(sorted(el)) for el in data_test[i]]
        d_o = ["".join(sorted(el)) for el in data_out[i]]
        num = [""]*10
        num[1] = find_one(d_t)
        num[4] = find_four(d_t)
        num[7] = find_seven(d_t)
        num[8] = find_eight(d_t)
        num[6] = find_six(d_t, num[7])
        num[9] = find_nine(d_t, num[4])
        num[3] = find_three(d_t, num[7])
        num[5] = find_five(d_t, num[6])
        num[0] = find_zero(d_t, num[6], num[9])
        num[2] = find_two(d_t, num[3], num[5])
        total += get_output(d_o, num)
    return total

def get_output(data, num):
    number = ""
    for el in data:
        # Concat index that element is at in number list
        number += str(num.index(el))
    return int(number)

def find_zero(data, six, nine):
    return [el for el in data 
        if (el != six and el != nine
        and len(el) == 6)
    ][0]

def find_one(data):
    return [el for el in data if len(el)==2][0]

def find_two(data, three, five):
    return [el for el in data 
        if el != three and el != five
        and len(el) == 5
    ][0]

def find_three(data, seven):
    return [el for el in data 
        if len(set(el) & set(seven)) == 3
        and len(el) == 5
    ][0]

def find_four(data):
    return [el for el in data if len(el)==4][0]

def find_five(data, six):
    return [el for el in data 
        if len(set(el) & set(six)) == 5
        and len(el) == 5
    ][0]

def find_six(data, seven):
    return [el for el in data 
        if len(set(el) & set(seven)) == 2
        and len(el) == 6
    ][0]

def find_seven(data):
    return [el for el in data if len(el)==3][0]

def find_eight(data):
    return [el for el in data if len(el)==7][0]

def find_nine(data, four):
    return [el for el in data 
        if len(set(el) & set(four)) == 4
        and len(el) == 6
    ][0]

if __name__ == '__main__':
    main()