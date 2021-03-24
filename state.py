class State:
    def __init__(self, transitions, isStart, isAccept):
        self.transitions = transitions
        self.isStart = isStart
        self.isAccept = isAccept

    def getTransitions(self):
        return self.transitions

    def getIsStart(self):
        return self.isStart

    def getIsAccept(self):
        return self.isAccept