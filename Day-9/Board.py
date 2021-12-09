class Board():
    def __init__(self, data):
        self.data = data
        self.s = (len(data), len(data[0]))
        self.low_points_value = 0
        self.setup()

    def setup(self):
        self.checked = [[False for j in range(self.s[1])]for i in range(self.s[0])]
        return
    
    def get_element(self, p):
        return self.data[p[0]][p[1]]
    
    def find_basin_length(self, p_in):
        self.checked[p_in[0]][p_in[1]] = True
        total = 1
        ind_adj = [(p_in[0] -1, p_in[1]), (1 + p_in[0], p_in[1]),
                    (p_in[0], p_in[1]-1), (p_in[0], 1 + p_in[1])]
        for p in ind_adj:
            if not self.inside_grid((p[0], p[1]), self.s):
                continue
            if not self.checked[p[0]][p[1]] and self.data[p[0]][p[1]] != 9:
                total += self.find_basin_length(p)
        return total
    
    def find_low_points(self):
        low_points = []
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                el = self.data[i][j]
                ind_adj = [(i -1, j), (1 + i, j),
                            (i, j-1), (i, 1 + j)]
                adj = []
                for p in ind_adj:
                    if self.inside_grid((p[0], p[1]), self.s):
                        adj.append(self.data[p[0]][p[1]])
                if min(adj) > el:
                    low_points.append((i,j))
                    self.low_points_value += el + 1
        return low_points
    
    def get_sum_of_low_points(self):
        return self.low_points_value

    def inside_grid(self, p, s):
        if p[0] < 0 or p[0] >= s[0]:
            return False
        if p[1] < 0 or p[1] >= s[1]:
            return False
        return True