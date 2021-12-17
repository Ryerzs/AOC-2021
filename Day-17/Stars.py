import time
import math

def main():
    path = "data.txt"
    # path = "test-data.txt"
    split = open(path, 'r').read().splitlines()[0].split(" ")
    start_time = time.time()
    x = (split[2][2:]).split('..')
    y = (split[3][2:]).split('..')
    x = (int(x[0]), int(x[1][:-1]))
    y = (int(y[1]), int(y[0]))

    x_poss = find_possible_x(x)

    N = 180
    highest_y = 0
    c = 0
    for x_try in range(x_poss[0], x_poss[1]+1):
        y_try = -30
        while y_try < N:
            test_vel = (x_try, y_try)
            hit, new_high = hits_range_highest(test_vel, x, y)
            if hit:
                if new_high > highest_y:
                    highest_y = new_high
                c+= 1
            y_try+= 1
    N = 0
    for x_try in range(x_poss[1]+1, x_poss[1]+ 100):
        y_try = -180
        while y_try < N:
            test_vel = (x_try, y_try)
            c += int(hits_range(test_vel, x, y))
            y_try+= 1

    dt = time.time() - start_time
    print(dt)
    print(highest_y)
    print(c)

def find_possible_x(x_range):
    x_lower = math.ceil(-1/2 + math.sqrt(2*x_range[0] + 1/4))
    x_upper = math.floor(-1/2 + math.sqrt(2*x_range[1] + 1/4))
    return (x_lower, x_upper)

def hits_range(vel, x_range, y_range):
    x_vel = vel[0]
    y_vel = vel[1]
    x_pos = 0
    y_pos = 0
    while y_pos > y_range[1]:
        x_pos += x_vel
        y_pos += y_vel
        x_vel -= not not x_vel
        y_vel -= 1
        if y_pos >= y_range[1] and y_pos <= y_range[0]:
            if x_pos >= x_range[0] and x_pos <= x_range[1]:
                return True
    return False

def hits_range_highest(vel, x_range, y_range):
    x_vel = vel[0]
    y_vel = vel[1]
    x_pos = 0
    y_pos = 0
    highest_y = 0
    while y_pos > y_range[1]:
        x_pos += x_vel
        y_pos += y_vel
        if y_pos > highest_y:
            highest_y = y_pos
        x_vel -= not not x_vel
        y_vel -= 1
        if y_pos >= y_range[1] and y_pos <= y_range[0]:
            if x_pos >= x_range[0] and x_pos <= x_range[1]:
                return True, highest_y
    return False, None

if __name__ == '__main__':
    main()