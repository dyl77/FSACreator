from state import *
from transition import *

class Runner:
    def __init__(self, startState):
        self.startState = startState
        self.currentState = startState

    def getCurrentState(self):
        return self.currentState
    
    def checkIfAccept(self):
        if self.currentState.getIsAccept():
            return True
        else:
            return False

    def changeStateIfValid(self, toState, letter):
        transitions = self.currentState.getTransitions()
        for transition in transitions:
            if transition.getTransitionLetter() == letter:
                self.currentState = transition.getToState()
                return self.currentState()
        return -1


    