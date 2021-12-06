import time

def main():
    path = "data.txt"
    lines = [int(row) for row in open(path, "r",encoding="utf-8").readlines()]

    start_time = time.time()
    # Star 1 with list-comprehension
    sum_1 = sum([lines[i] < lines[i+1] for i in range(len(lines)-1)])
    # Star 2 with list-comprehension
    data = [sum([row for row in lines[i:i+3]]) for i in range(len(lines)-2)]
    sum_2 = sum([data[i] < data[i+1] for i in range(len(data)-1)])
    dt = time.time() - start_time
    print("Shifting sum:", sum_1)
    print("Regular sum:", sum_2)
    print(dt)
    

if __name__ == "__main__":
    main()