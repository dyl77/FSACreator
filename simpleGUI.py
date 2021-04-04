from tkinter import *
from state import *
from transition import *
from tkinter import messagebox
from automataBuilder import listToString

root = Tk()
root.geometry("500x1000")
root.title("PL P3: FSA Creator")
circles = list()
myCanvas = Canvas(root)
myCanvas.pack(expand = True, fill = "both")

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def drawStates(stateCount, stateList):
    baseYCord = 50
    x = 0
    while x<stateCount:
        id = create_circle(100, baseYCord, 30, myCanvas)
        circles.append(id)
        baseYCord += 100
        if stateList[x].getIsAccept() == 1:
            create_circle(100, baseYCord, 35, myCanvas)
        if stateList[x].getIsStart() == 1:
            toCoords = myCanvas.coords(circles[x])
            myCanvas.create_line(0, 0, toCoords[0], toCoords[1], arrow= "last")
        x += 1

def drawTransitions(stateList):
    for state in stateList:
       transitions = state.getTransitions()
       for transition in transitions:
            if transition.getToState() == transition.getFromState():
                fromCoords = myCanvas.coords(circles[int(transition.getFromState())])
                ycoord = (fromCoords[1] + fromCoords[3])/2
                newid = create_circle(fromCoords[2],ycoord, 20, myCanvas)
                newCircleCoords = myCanvas.coords(newid)
                myCanvas.create_line(newCircleCoords[0], newCircleCoords[1], newCircleCoords[0]-10, newCircleCoords[1], arrow= "last")
                label = Label(root, text=str(transition.getTransitionLetter()))
                label.place(x=newCircleCoords[0]+35, y= newCircleCoords[1]+35)
            else:
                fromCoords = myCanvas.coords(circles[int(transition.getFromState())])
                toCoords = myCanvas.coords(circles[int(transition.getToState())])
                lineid = myCanvas.create_line(fromCoords[0], fromCoords[1], toCoords[0], toCoords[1], arrow= "last")
                label = Label(root, text=str(transition.getTransitionLetter()))
                labelx = (fromCoords[0] + toCoords[0])/2
                labely = (fromCoords[1] + toCoords[1])/2
                label.place(x=labelx, y= labely)


def labelStates(stateCount):
    i = 0
    while i < stateCount:
        theCoords = myCanvas.coords(circles[i])
        label = Label(root, text=str(i))
        midx = (theCoords[0]-10 + theCoords[2])/2
        midy = (theCoords[1]-10 + theCoords[3])/2
        label.place(x=midx, y=midy)
        i += 1


def showFSAAccepted(string):
    messagebox.showinfo("Congratulations!", "The string: " + listToString(string) + " was accepted by the current FSA!")

def showFSANotAccepted(string, state):
    messagebox.showerror("String not accepted", "The string: " + listToString(string) + " is not accepted by current automata => State: " + str(state) + " Is not an accepting state.")

def showFSAError(string, state, char):
    messagebox.showerror("Invalid transition", "String is not accepted by current automata => Invalid char: " + char + " " + "from state: " + str(state))

def drawFSA():
    root.mainloop()
