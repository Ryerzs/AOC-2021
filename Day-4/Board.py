class Board():
    def __init__(self, l, board_number):
        self.l = l
        self.last_drawn = 0
        self.board_number = board_number
        self.won_state = False
    
    def has_won(self) -> bool:
        # Counts how many marked squares are in each row
        row_marked = [sum([1 for el in row if el == ""])
                        for row in self.l]
        # Counts how many marked squares are in each column
        col_marked = [sum([1 for row in self.l if row[i] == ""])
                        for i in range(len(self.l[0]))]
        # If either col or row contain a 5, the board has won
        if 5 in col_marked or 5 in row_marked:
            return True
        return False
    def change_won_state(self, b : bool):
        self.won_state = b

    # Updates board with new drawn number.
    # Also stores the number drawn for use in sum_won()
    def draw_new_number(self, n):
        self.last_drawn = n
        self.l = [[el if el != n else "" for el in row]
                    for row in self.l]

    # Sums all unmarked numbers
    def sum_of_unmarked(self) -> int:
        unmarked_sum = sum([sum([el for el in row if el != ""])
                        for row in self.l])
        return(unmarked_sum)

    # Returns computed solution
    def sum_won(self) -> int:
        return(self.sum_of_unmarked() * self.last_drawn)