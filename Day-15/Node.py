class Node():
    def __init__(self, ind, val):
        self.ind = ind
        self.neigh = []
        self.val = val
    
    def add_negihbors(self, neigh):
        for n in neigh:
            if n not in self.neigh:
                self.neigh.append(n)
                n.neigh.append(self)
    
    def print_neighbors(self):
        for n in self.neigh:
            print(n.ind)
            