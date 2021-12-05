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
    print("Time:",dt) # Time is ~75ms
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
        l = len(boards)
        # Update all boards
        for j in range(l):
            boards[j].draw_new_number(numbers_draw[i])
            if boards[j].has_won():
                boards[j].change_won_state(True)
        if l == 1 and boards[0].won_state:
            return str(boards[0].board_number) + " " + str(boards[0].sum_won())
        # Keep boards that havn't won yet
        
        boards = [b for b in boards if b.won_state == False]

if __name__ == '__main__':
    main()