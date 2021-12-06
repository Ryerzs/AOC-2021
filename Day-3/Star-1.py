
def main():
    # path = "Day-3/test-data.txt"
    path = "data.txt"
    lines = [[int(el) for el in row] for row in open(path, "r",encoding="utf-8").read().splitlines()]
    print(lines)
    gamma = [int(sum(el[i] for el in lines)>len(lines)/2)
        for i in range(len(lines[0]))]
    # epsilon = [(el+1)%2 for el in gamma]
    gamma_dec = sum([gamma[-i-1]*2**(i) for i in range(len(gamma))])
    print(gamma_dec)
    epsilon_dec = 2**(len(gamma)) - gamma_dec -1
    # Convert list of bits to product in decimal
    answer = []
    print(gamma_dec * epsilon_dec)

if __name__ == '__main__':
    main()