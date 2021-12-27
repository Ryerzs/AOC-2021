class Box():
    def __init__(self, val, ranges):
        self.ranges = ranges
        self.val = val
    
    def getVolume(self):
        if not self.val:
            return 0
        x = self.getIntervallLength(0)
        y = self.getIntervallLength(1)
        z = self.getIntervallLength(2)
        return x*y*z
    
    def getIntervallLength(self, ind):
        cRange = self.getRange(ind)
        upper = cRange[1]
        lower = cRange[0]
        length = upper - lower + 1
        return length
    
    def getRange(self, ind):
        return self.ranges[ind]