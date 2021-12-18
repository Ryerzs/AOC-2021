class Performed_Action():
    def __init__(self, state: bool = False):
        self.state = state
    
    def setState(self, state: bool):
        self.state = state
    
    def getState(self):
        return self.state