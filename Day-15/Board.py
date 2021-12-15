from Node import *

class Board():
    def __init__(self, s, vals):
        self.s = s
        self.setup(vals)
    
    def setup(self, vals):
        self.grid = [[Node((i, j), vals[i][j]) for j in range(self.s[1])]
                     for i in range(self.s[0])]
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                adj = self.get_adj(i, j)
                for p in adj:
                    if self.inside_grid((p[0], p[1])):
                        self.grid[i][j].add_negihbors([self.grid[p[0]][p[1]]])
    
    def print_grid(self):
        for i in range(self.s[0]):
            s = ''
            for j in range(self.s[1]):
                s += str(self.grid[i][j].val)
            print(s)

    def get_adj(self, i, j):
        adj = [ (i + 1, j),
                (i    , j + 1),
                (i - 1, j),
                (i    , j - 1),
        ]
        return(adj)

    def inside_grid(self, p):
        if p[0] < 0 or p[0] >= self.s[0]:
            return False
        if p[1] < 0 or p[1] >= self.s[1]:
            return False
        return True