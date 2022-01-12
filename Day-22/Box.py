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
    
    def getIntervallLength(self, dim):
        cRange = self.getRange(dim)
        upper = cRange[1]
        lower = cRange[0]
        length = upper - lower + 1
        return length
    
    def getRange(self, dim):
        return self.ranges[dim]
    
    def getCorner(self, upperX, upperY, upperZ):
        x = self.getRange(0)[upperX]
        y = self.getRange(1)[upperY]
        z = self.getRange(2)[upperZ]
        return [x, y, z]