class Transition:
    def __init__(self, fromState, toState, transitionLetter):
        self.fromState = fromState
        self.toState = toState
        self.transitionLetter = transitionLetter

    def getFromState(self):
        return self.fromState

    def getToState(self):
        return self.toState

    def getTransitionLetter(self):
        return self.transitionLetter