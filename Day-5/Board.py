class Board():
    def __init__(self, s):
        self.s = s
        self.setup()
    
    def setup(self):
        self.board = [  [0 for j in range(self.s)]
                        for i in range(self.s)]
    def add_line(self, l, star_2 : bool):
        points = None
        # x is constant
        if(l[0][0] == l[1][0]):
            x = l[0][0]
            y1 = min(l[0][1], l[1][1])
            y2 = max(l[0][1], l[1][1])
            points = [[x,y] for y in range(y1, y2+1)]
        # y is constant
        elif(l[0][1] == l[1][1]):
            y = l[0][1]
            x1 = min(l[0][0], l[1][0])
            x2 = max(l[0][0], l[1][0])
            points = [[x,y] for x in range(x1, x2+1)]
        # Else its on the diagonal
        elif star_2:
            if l[0][0] < l[1][0]:
                x1, y1 = l[0][0], l[0][1]
                x2, y2 = l[1][0], l[1][1]
            else:
                x2, y2 = l[0][0], l[0][1]
                x1, y1 = l[1][0], l[1][1]
            # y2-y1 = x2-x1
            points = [[x,self.line_form(x,x1,x2,y1,y2)] for x in range(x1,x2+1)]
        if points == None:
            return
        for p in points:
            self.board[p[1]][p[0]] += 1
    
    def line_form(self, x, x1, x2, y1, y2):
        k = (y2-y1)/(x2-x1)
        return int(k*(x-x1) + y1)

    
    def get_overlap_count(self):
        count = sum([sum([1 for el in row if el >= 2]) for row in self.board])
        return(count)