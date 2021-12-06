def main():
    path = "data.txt"
    lines = [[el for el in row.split()] for row in open(path, "r",encoding="utf-8").read().splitlines()]
    lines = [[int(row.split()[1]),0]
                if row.split()[0] == "forward" else (
                [0, int(row.split()[1])]
                if row.split()[0] == "down" else 
                [0, -int(row.split()[1])]
                )
            for row in open(path, "r",encoding="utf-8").read().splitlines()]
    aim = 0
    pos = [0, 0]
    for i in range(len(lines)):
        command = lines[i]
        aim += command[1]
        pos = [pos[0] + command[0], pos[1] + command[0]*aim]
    print(pos)
    print(pos[0]*pos[1])

if __name__ == '__main__':
    main()
                    # (0, int(el[1])) if el[0] == "down" 
                    # else (0, -int(el[1]))
                    # )