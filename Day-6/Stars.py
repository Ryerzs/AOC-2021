import time

def main():
    path = "data.txt"
    data_in = [int(el) for el in open(path, 'r').read().splitlines()[0].split(",")]
    start_time = time.time()
    # Create data list
    data = [0] * 9
    # foreach squid at day i, increase index i by one
    for el in data_in:
        data[el] += 1
    # Iterate through each day
    days = 256
    for _ in range(days):
        # Pop previous day, essentially shifting all days forward
        new = data.pop(0)
        # Add the amount that was on the previous day to day 6
        # and to new squids
        data[6] += new
        data.append(new)
    dt = time.time() - start_time
    print(dt) # ~The only value I've gotten is 0.99 ms so I'll go with 1 ms
    print(sum(data))

if __name__ == '__main__':
    main()