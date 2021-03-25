class State:
    def __init__(self): #, transitions, isStart, isAccept):
        self.transitions = None
        self.isStart = 0
        self.isAccept = 0

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