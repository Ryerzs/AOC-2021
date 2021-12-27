from collections import deque
class Instruction():
    def __init__(self):
        self.input = deque([])
        self.type = None
        self.var = None
        self.val = None
    
    def setInput(self, inp):
        self.input = inp

    def setVariables(self, var):
        self.variables = var
    
    def getNextInput(self):
        return self.input.popleft()
    
    def performInstruction(self):
        if self.type == 'inp':
            self.performInput()
        elif self.type == 'add':
            self.performAdd()
        elif self.type == 'mul':
            self.performMul()
        elif self.type == 'mod':
            self.performMod()
        elif self.type == 'div':
            self.performDiv()
        elif self.type == 'eql':
            self.performEql()
        
    
    def performInput(self):
        inp = self.getNextInput()
        self.variables[self.var] = inp
    
    def getValue(self):
        if self.val.isnumeric():
            return int(self.val)
        elif self.val[1:].isnumeric():
            return int(self.val)
        return self.variables[self.val]

    def performAdd(self):
        val = self.getValue()
        self.variables[self.var] = self.variables[self.var] + val

    def performMul(self):
        val = self.getValue()
        self.variables[self.var] = self.variables[self.var] * val

    def performMod(self):
        val = self.getValue()
        self.variables[self.var] = self.variables[self.var] % val

    def performDiv(self):
        val = self.getValue()
        self.variables[self.var] = self.variables[self.var] // val

    def performEql(self):
        val = self.getValue()
        self.variables[self.var] = int(self.variables[self.var] == val)