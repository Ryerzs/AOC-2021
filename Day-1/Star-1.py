
def main():
    path = "measurements.txt"
    data = load_data(path)
    count = count_increasing_iterations(data)
    print(count)

# TODO: Implement a way to load data from txt file
def load_data(path: str) -> list:
    pass

# TODO: Iterate through data vector and count increases in next iteration
def count_increasing_iterations(data: list) -> int:
    pass

if __name__ == "__main__":
    main()