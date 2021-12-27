from Node import *
class Graph():
    def __init__(self, rooms, data):
        self.rooms = rooms
        self.points = []
        self.setup()
    
    def setup(self):
        for i in range(self.rooms*2+3):
            self.points.append(Node())