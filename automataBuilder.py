def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string
    #print(str1)   
    return str1  

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


fname = 'legal.txt'

out = open('out.txt','w')

total = 0

with open(fname) as f:
    content = f.readlines()

inputString = listToString(content)
splitBySemicolon = inputString.split(";")

firstParensIndex = splitBySemicolon[2].split(",")


for parts in splitBySemicolon:
    
    print(parts)
    
        
#out.write('\n')
# out.write(str(total))
out.close()
f.close()

        