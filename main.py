from automataBuilder import *
from automataRunner import *

stateList = buildAutomata()
# print(getStartState(stateList))
startState = getStartState(stateList)
autoRunner = Runner(startState, stateList)



chars = getInputChars("illegal.txt")

# result = autoRunner.changeState("x")


for char in chars:
    if char == '':
        if autoRunner.checkIfAccept() == True:
            print("String is accepted by current automata")
            exit()
        else:
            print("String is not accepted by current automata => State: " + str(autoRunner.currentState.getStateNumber()) + " Is not an accepting state.")
            exit()
    
    
    result = autoRunner.changeState(char)
    # result = autoRunner.changeStateIfValid(char)
    # print("Current State: " + str(autoRunner.currentState.getStateNumber()) + " Char: " + char + " " + str(result))
    if result == -1:
        print("String is not accepted by current automata => Invalid char: " + char + " " + "from state: " + str(autoRunner.currentState.getStateNumber()))
        break

        

    

  