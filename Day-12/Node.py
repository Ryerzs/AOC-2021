import copy
class Node():
    def __init__(self, name: str, big: bool, ind: int):
        self.name = name
        self.big = big
        self.neigh = []
        self.neigh_names = []
        self.passed = 0
        self.all = []
        self.ind = ind
        self.len_all = 0
    
    def add_neighbor(self, neighbor):
        if not neighbor.name in self.neigh_names:
            self.neigh.append(neighbor)
            self.neigh_names.append(neighbor.name)
            neighbor.add_neighbor(self)
    def set_ref_to_all(self, all_n):
        self.all = all_n
        self.len_all = len(all_n)
    
    def get_neigh_names(self):
        return self.neigh_names
    
    def find_path(self, cur):
        if len(cur) > 400:
            return "Stop"
        if self.passed > 0 and not self.big:
            return 0
        if self.name == 'end':
            return 1
        tot = 0
        self.passed += 1
        cur.append(self)
        for n in self.neigh:
            # v = n.find_path(cur[:])
            # if v == "Stop":
            #     print("Called stop")
            #     return "Stop"
            # tot += v
            tot += n.find_path(cur[:])
        self.passed -= 1
        return tot

    def find_path_2(self, cur):
        if self.name == 'start':
            if self.passed > 0:
                return 0
        if self.name == 'end':
            return 1
        if self.small_cave_in_list(cur):
            if not self.big:
                if self.passed > 0:
                    return 0
        else:
            if not self.big:
                if self.passed > 1:
                    return 0
        tot = 0
        self.passed += 1
        cur.append(self)
        for n in self.neigh:
            tot += n.find_path_2(cur)
        cur.pop()
        self.passed -= 1
        return tot
    
    def print_node_list(self, node_list):
        s = ""
        for n in node_list:
            s += n.name + " "
        print(s)
    
    def small_cave_in_list(self, l):
        node_count = [0] * self.len_all
        for n in l:
            node_count[n.ind] += 1
            if node_count[n.ind] < 2:
                continue
            if not self.all[n.ind].big:
                return True

        return False