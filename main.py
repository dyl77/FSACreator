from automataBuilder import *
from automataRunner import *
from simpleGUI import *
import sys

stateList = buildAutomata(sys.argv[1])
startState = getStartState(stateList)
autoRunner = Runner(startState, stateList)

drawStates(len(stateList), stateList)
drawTransitions(stateList)
labelStates(len(stateList))
drawFSA() 

chars = getInputChars(sys.argv[2])

for char in chars:
    if char == '':
        if autoRunner.checkIfAccept() == True:
            print("String: "+ listToString(chars) +" is accepted by current automata.")
            # showFSAAccepted(chars)
            exit()
        else:
            print("String: "+ listToString(chars) + " is not accepted by current automata => State: " + str(autoRunner.currentState.getStateNumber()) + " Is not an accepting state.")
            # showFSANotAccepted(chars, autoRunner.currentState.getStateNumber())
            exit()
     
    result = autoRunner.changeState(char)
    if result == -1:
        print("String is not accepted by current automata => Invalid char: " + char + " " + "from state: " + str(autoRunner.currentState.getStateNumber()))
        # showFSAError(chars, autoRunner.currentState.getStateNumber(), char)
        break

        

    

  