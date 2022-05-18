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
    
    def splitAt(self, corner):
        boxes = []
        ranges = self.getNewRanges(corner)
        print(ranges)
        for r in ranges:
            boxes.append(Box(1, r))
        return boxes
    
    def getNewRanges(self, corner):
        ranges = []
        xr = [[self.ranges[0][0], corner[0] -1 ], [corner[0], self.ranges[0][1]]]
        zr = [[self.ranges[1][0], corner[1] -1 ], [corner[1], self.ranges[1][1]]]
        yr = [[self.ranges[2][0], corner[2] -1 ], [corner[2], self.ranges[2][1]]]
        for xi in range(2):
            for yi in range(2):
                for zi in range(2):
                    ranges.append([xr[xi], yr[yi], zr[zi]])
        return ranges
    