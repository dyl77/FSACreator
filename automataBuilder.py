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
            if state.getStateNumber() == transition.getFromState():
                state.addTransition(transition)



##### End processing of string to get info about FA ######

fname = 'legal.txt'

out = open('out.txt','w')

total = 0

with open(fname) as f:
    content = f.readlines()

inputString = listToString(content)
splitBySemicolon = inputString.split(";")

stateCount = processStateCount(splitBySemicolon)
stateList = createStates(stateCount)
transitionContainer = createTransitions(splitBySemicolon)
addTransitionsToStates(stateList, transitionContainer)



for parts in splitBySemicolon:
    pass
    # print(parts)
    
        
#out.write('\n')
# out.write(str(total))
out.close()
f.close()

        