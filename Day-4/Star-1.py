from Board import *
import time

def main():
    path = "Day-4/data.txt"
    lines = open(path, "r",encoding="utf-8").read().splitlines()

    start_time = time.time()
    numbers_draw = [int(el) for el in lines[0].split(",")]
    boards = load_boards(lines)
    str_out = start_game(numbers_draw, boards)
    dt = time.time() - start_time
    print("Time:",dt) # Time is ~24ms
    print(str_out)

def load_boards(lines):
    board_lists = []
    boards = []
    # For loop with length of number of boards
    for i in range(len(lines)//6):
        board_lists.append([[int(el) for el in row.split()]
                            for row in lines[i*6 + 2 : i*6 + 7]])
        boards.append(Board(board_lists[i], i + 1))
    return(boards)

def start_game(numbers_draw, boards) -> str:
    # Draw numbers for all boards
    for i in range(len(numbers_draw)):
        # Update all boards
        for j in range(len(boards)):
            boards[j].draw_new_number(numbers_draw[i])
            # End if a board has won
            if boards[j].has_won():
                return str(j) + " " + str(boards[j].sum_won())

if __name__ == '__main__':
    main()