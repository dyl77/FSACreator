from state import *
from transition import *

def listToString(s):  
    
    str1 = ""  
     
    for ele in s:  
        str1 += ele   
    
    # return string
    #print(str1)   
    return str1  

##### Processing String to get info about FA #####
def processStateCount(stringSplitBySemicolon):
    stateCount = stringSplitBySemicolon[0]

    return stateCount

def processAlphabet(stringSplitBySemicolon):
    alphabet = stringSplitBySemicolon[1].split(",")

    return alphabet

def processTransitions(stringSplitBySemicolon):
    #construct a transition here
    return 0

def processStartState(stringSplitBySemicolon):
    startState = stringSplitBySemicolon[3]

    return startState

def processAcceptStates(stringSplitBySemicolon):
    acceptStates = stringSplitBySemicolon[4].split(",")

    return acceptStates

def createStates(stateCount):
    i = 0
    stateList = list()

    while i < int(stateCount):
        stateList.append(State(i))
        i +=1

    return stateList

def createTransitions(stringSplitBySemicolon):
    transitions = stringSplitBySemicolon[2].split(",")
    transitionContainer = list()

    for parts in transitions:
        singleParts = parts.split(":")
        singleParts[0] = singleParts[0].replace("(", "")
        singleParts[2] = singleParts[2].replace(")", "")
        # print(singleParts)
        transitionContainer.append(Transition(singleParts[0], singleParts[1], singleParts[2]))

    return transitionContainer

def addTransitionsToStates(stateList, transitionContainer):

    for transition in transitionContainer:
        for state in stateList:
            if state.getStateNumber() == int(transition.getFromState()):
                state.addTransition(transition)

def setStartState(stateList, startStateNo):
    for state in stateList:
        if(state.getStateNumber() == int(startStateNo)):
            state.setIsStart()

def setAcceptStates(stateList, acceptStateNumbers):
    for stateNumbers in acceptStateNumbers:
        for state in stateList:
            if state.getStateNumber() == int(stateNumbers):
                state.setIsAccept()

def getStartState(stateList):
    for state in stateList:
        if(state.getIsStart()):
            return state

def getInputChars(filename):
    chars = list()
    file = open(filename, 'r')
  
    while 1:
        # read by character
        char = file.read(1)
        chars.append(char)          
        if not char: 
            break
    #chars.remove('')
    return chars


def buildAutomata():
    fname = 'fsa.txt'

    with open(fname) as f:
        content = f.readlines()

    inputString = listToString(content)
    splitBySemicolon = inputString.split(";")

    # Put into configureAutomata def
    stateCount = processStateCount(splitBySemicolon)
    stateList = createStates(stateCount)
    transitionContainer = createTransitions(splitBySemicolon)
    addTransitionsToStates(stateList, transitionContainer)

    startStateNo = processStartState(splitBySemicolon)
    acceptStateNumbers = processAcceptStates(splitBySemicolon)

    setStartState(stateList, startStateNo)
    setAcceptStates(stateList, acceptStateNumbers)

    
    # for parts in stateList:
    #     print("State No: " + str(parts.getStateNumber()) + " Is Start?: " + str(parts.getIsStart()) + " Is Accept?: " + str(parts.getIsAccept()) + "\n")

    f.close()
    return stateList



##### End processing of string to get info about FA ######

#Set up loop to read chars from input string for processing
#Make legal and illegal string
#Send char to start state (Debug: send legal or illegal char to console)
#Make next state function, where it returns illegal (-1) or legal state number &  (DONE)
#Test if end of string and ask if accept state, if not not accepted string (DONE)
    