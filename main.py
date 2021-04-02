from automataBuilder import *
from automataRunner import *
import sys

stateList = buildAutomata(sys.argv[1])
startState = getStartState(stateList)
autoRunner = Runner(startState, stateList)

chars = getInputChars(sys.argv[2])

for char in chars:
    if char == '':
        if autoRunner.checkIfAccept() == True:
            print("String is accepted by current automata")
            exit()
        else:
            print("String is not accepted by current automata => State: " + str(autoRunner.currentState.getStateNumber()) + " Is not an accepting state.")
            exit()
     
    result = autoRunner.changeState(char)
    if result == -1:
        print("String is not accepted by current automata => Invalid char: " + char + " " + "from state: " + str(autoRunner.currentState.getStateNumber()))
        break

        

    

  