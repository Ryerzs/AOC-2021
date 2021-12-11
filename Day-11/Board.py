class Board():
    def __init__(self, data):
        self.data = data
        self.s = (len(data), len(data[0]))
        self.low_points_value = 0
        self.flash_count = 0
        self.setup()

    def setup(self):
        self.checked = [[0] * self.s[1] for i in range(self.s[0])]
        self.flashed = [[0] * self.s[1] for i in range(self.s[0])]
        return
    
    def print(self):
        for i in range(self.s[0]):
            print(self.data[i])
    
    def step(self, step):
        for i in range(step):
            self.simulate_step()
            if self.all_zero():
                return i+1
        return -1
    
    def all_zero(self):
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                if self.data[i][j] != 0:
                    return False
        return True
    
    def simulate_step(self):
        self.checked = [[0] * self.s[1] for i in range(self.s[0])]
        self.flashed = [[0] * self.s[1] for i in range(self.s[0])]
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                self.checked[i][j] = True
                self.increase_energy(i,j)
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                if self.flashed[i][j]:
                    self.data[i][j] = 0

    def increase_energy(self, i, j):
        self.data[i][j] += 1
        if self.data[i][j] > 9 and not self.flashed[i][j]:
            self.flash_count += 1
            self.data[i][j] = 0
            self.flashed[i][j] = True
            adj = self.get_adj(i, j)
            for p in adj:
                if not self.inside_grid((p[0], p[1])):
                    continue
                if not self.flashed[p[0]][p[1]]:
                    self.increase_energy(p[0], p[1])
    
    def get_adj(self, i, j):
        adj = [ (i + 1, j),
                (i + 1, j + 1),
                (i    , j + 1),
                (i - 1, j + 1),
                (i - 1, j),
                (i - 1, j - 1),
                (i    , j - 1),
                (i + 1, j - 1),
        ]
        return(adj)

    def inside_grid(self, p):
        if p[0] < 0 or p[0] >= self.s[0]:
            return False
        if p[1] < 0 or p[1] >= self.s[1]:
            return False
        return True