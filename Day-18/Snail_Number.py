import copy
from Performed_Action import *
class Snail_Number():
    def __init__(self, inp: 'list', depth: int = 1, direction: int = 0):
        self.depth = depth
        self.children = []
        self.isVal = False
        self.performed = False
        self.val = 0
        # 0 -> Left
        # 1 -> Right
        self.dir = direction
        if inp != []:
            self.parse_children(inp)
    
    # Takes list 
    def parse_children(self, inp: 'list'):
        if type(inp) is int:
            self.val = inp
            self.isVal = True
            return
        for i, iv in enumerate(inp):
            self.children.append(Snail_Number(iv, self.depth + 1, i))
    
    # Stabilizes snail number
    def reduce(self):
        """
        Reduce tries to reduce the snail number. It tries two actions,
        namely, exploding and splitting, in that order.
        So it explodes until it can't anymore, and then tries to split.
        Then it tries exploding again, and so on.
        """
        run = True
        while self.performed_action() or run:
            if not run:
                self.reset_performed()
            run = False
            self.try_explode()
            # If it couldn't explode, try splitting
            if not self.performed_action():
                run = self.try_split()

    # Tries to explode snail numbers from left to right
    def try_explode(self):
        instructions = []
        # If we are deep enough and have reached a number pair
        # then we explode
        if self.depth > 4 and self.children_are_values():
            self.performed = True
            return 'explode'
        # Loop through children and see if they explode
        for cv in self.children:
            action = []
            if cv.isVal:
                continue
            action = cv.try_explode()
            # Child want's to explode, so as a doting parent, we let help it
            if action == 'explode':
                # It will bubble up a value to give to another snail number
                instructions.append(self.explode_child(cv))
            # If instead the child is bubbling up a pair that has
            # exploded further down, we check if we can take care
            # of it, or if we need to bubble it further up.
            elif isinstance(action, list):
                for t in action:
                    # If it for example came from the right and wants
                    # to append number in the same direction, then
                    # we need to bubble up further
                    if cv.dir == t[0]:
                        instructions.append(t)
                    else:
                        # Add number to opposite side it came from
                        if t[0]:
                            self.children[t[0]].add_left_most(t[1])
                        else:
                            self.children[t[0]].add_right_most(t[1])
        return instructions 
    
    def try_split(self):
        if self.isVal and self.val > 9:
            inp = [0, 0]
            inp[0] = self.val // 2
            inp[1] = self.val - inp[0]
            self.val = 0
            self.isVal = False
            for i, iv in enumerate(inp):
                self.children.append(Snail_Number(iv, self.depth + 1, i))
            return True

        for cv in self.children:
            if cv.try_split():
                return True
        return False
    
    def performed_action(self):
        if self.performed:
            return True
        for cv in self.children:
            if cv.performed_action():
                return True
        return False
    
    def reset_performed(self):
        self.performed = False
        for cv in self.children:
            cv.reset_performed()
    
    def children_are_values(self):
        for cv in self.children:
            if not cv.isVal:
                return False
        return True
    
    def explode_child(self, child):
        leftv = child.children[0].val
        rightv = child.children[1].val
        child.children.clear()
        child.isVal = True
        child.val = 0
        if child.dir:
            self.children[0].add_right_most(leftv)
            return (child.dir, rightv)
        else:
            self.children[1].add_left_most(rightv)
            return (child.dir, leftv)

    def add_left_most(self, val):
        self.add_side_most(val, 0)

    def add_right_most(self, val):
        self.add_side_most(val, 1)
    
    def add_side_most(self, val, side: int):
        if self.isVal:
            self.val += val
            return
        self.children[side].add_side_most(val, side = side)
    
    def print_self_and_children(self):
        if self.isVal:
            return str(self.val)
        c = []
        strings = []
        for cv in self.children:
            c.append(cv.print_self_and_children())
        ch = '|-'
        if type(c[0]) is str:
            strings.append(ch + c[0])
        else:
            for row in c[0]:
                strings.append(ch + row)
        if type(c[1]) is str:
            strings.append(ch + c[1])
        else:
            for row in c[1]:
                strings.append(ch + row)
        strings.append('')
        if self.depth == 1:
            for row in strings:
                print(row)
        return(strings)

    def get_array(self):
        arr = []
        for cv in self.children:
            if cv.isVal:
                arr.append(cv.val)
                continue
            arr.append(cv.get_array())
        return arr
    
    def get_magnitude(self):
        if self.isVal:
            return self.val * (3 - self.dir)
        v = 0
        for cv in self.children:
            v += cv.get_magnitude()
        if self.depth == 1:
            return v
        return v * (3 - self.dir)

    def add_snail(self, second_snail):
        arr1 = self.get_array()
        arr2 = second_snail.get_array()
        return Snail_Number([arr1, arr2])
    
    def printDepths(self):
        print(self.depth)
        for cv in self.children:
            cv.printDepths()
    