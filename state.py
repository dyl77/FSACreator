class State:
    def __init__(self, stateNumber): #, transitions, isStart, isAccept):
        self.stateNumber = stateNumber
        self.transitions = list()
        self.isStart = 0
        self.isAccept = 0

    def getStateNumber(self):
        return self.stateNumber
    
    def getTransitions(self):
        return self.transitions

    def getIsStart(self):
        return self.isStart

    def getIsAccept(self):
        return self.isAccept

    def setTransitions(self, transitions):
        self.transitions = transitions

    def setIsStart(self, isStart):
        self.isStart = isStart

    def setIsAccept(self, isAccept):
        self.isAccept = isAccept

    def addTransiton(self, transition):
        self.transitions.append(transition)