from state import *
from transition import *
import copy

class Runner:
    def __init__(self, startState, stateList):
        self.startState = startState
        self.currentState = copy.deepcopy(startState)
        self.stateList = stateList

    def getCurrentState(self):
        return self.currentState
    
    def checkIfAccept(self):
        if self.currentState.getIsAccept():
            return True
        else:
            return False

    def setCurrentState(self, state):
        self.currentState = state


    def changeState(self, letter):
        transitions = self.currentState.getTransitions()

        for transition in transitions:
            if transition.getTransitionLetter() == letter:
                newStateNumber = transition.getToState()
                break
        else:
            return -1

        for states in self.stateList:
            if int(newStateNumber) == int(states.getStateNumber()):
                self.setCurrentState(states)
                return self.currentState.getStateNumber()

            


    