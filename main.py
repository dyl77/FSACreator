from automataBuilder import *
from automataRunner import *

stateList = buildAutomata()

autoRunner = Runner(getStartState(stateList))

chars = getInputChars("legal.txt")
print(chars)
  