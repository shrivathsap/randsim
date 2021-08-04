import random
import turtle
import time
import matplotlib.pyplot as plt
from IPython.display import clear_output
#------------------------------------------------colours and parameters---------------------------------------------
def setfore():
    global color1
    color1=input("Pen colour:")
    try:
        turtle.color(color1)
    except:
        print("Not a color.")
        setfore()
def setback():
    global color2
    color2=input("Background:")
    try:
        turtle.screensize(bg=color2)
    except:
        print("Not a color.")
        setback()
def setborder():
    global color3
    color3=input("Border colour:")
    try:
        turtle.color(color3)
    except:
        print("Not a color.")
        setborder()
def parameters():
    global stepsize, numsteps, border
    stepsize=int(input("Enter step size, preferrably less than 10(for appearance):"))
    numsteps=int(input("Enter number of steps to take:"))
    setfore()
    setback()
    border=input("Do you need borders? Y/N")
    if border=="y":
        setborder()
        yardsize()
    else:
        gameon()
def yardsize():
    global sidelength
    sidelength=int(input("Enter the dimensions of turtle yard:"))
    limit=(stepsize*((numsteps**(0.5))))
    if ((sidelength/2)%stepsize) != 0:
        print("Turtle yard is too small.")
        yardsize()
    elif sidelength<=2*limit:
        print("Turtle yard is too small.")
        yardsize()
    else:
        turtle.up()
        turtle.goto(-sidelength/2,-sidelength/2)
        turtle.down()
        turtle.color(color3)
        turtle.left(90)
        for i in range(0,4):
            turtle.forward(sidelength)
            turtle.right(90)
        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        gameon()
        
#-------------------------------------actual walk------------------------------------------------------------------------- 
went=[(0,0)]
steps=0
toplot=[]
turtle.ht()
def gameon():
    turtle.screensize(canvwidth=5000, canvheight=5000, bg=color2)
    turtle.color(color1)
    while steps<numsteps:
        move()
        #print(steps)
        #time.sleep(runtime)
        #clear_output()
    else:
#----------------------end of walk and plotting--------------------------------------------------
        xs=[x[0] for x in toplot]
        ys=[x[1] for x in toplot]
        plt.xlabel("No. of steps taken")
        plt.ylabel("Positive distance from origin")
        plt.title("Self avoiding random walk")
        plt.grid(True)
        plt.plot(xs, ys)
        plt.show()
        turtle.done()
#-----------------------------------undo------------------------------
def undo():
    turtle.color(color2)
    prev=went.index((turtle.xcor(), turtle.ycor()))#Gives the index of first appearance on the list
    turtle.goto(went[prev-1])
    global steps
    steps -= 1
    went.append((turtle.xcor(), turtle.ycor()))#So that if there is any further blocking it won't go diagonally to the previous position
    turtle.color(color1)
    move()
#--------------------------moves--------------------------------------------------------    
def move():
    #start=time.time()
    coordset=[(turtle.xcor()+stepsize, turtle.ycor()), (turtle.xcor()-stepsize, turtle.ycor()), 
            (turtle.xcor(), turtle.ycor()+stepsize), (turtle.xcor(), turtle.ycor()-stepsize)]
    global coords
    coords=[]
    global went
    for i in range(len(coordset)):
        if coordset[i] not in went:
            coords.append(coordset[i])
    if border=="y":
        ifbordered()
    if len(coords) != 0:
        index=random.randint(0, len(coords)-1)
        turtle.goto(coords[index])
        went.append(coords[index])
        global steps
        steps += 1
        dist=(turtle.xcor()**2+turtle.ycor()**2)**(0.5)
        toplot.append((steps, dist))
    else:
        went.append((turtle.xcor(), turtle.ycor()))
        undo()
    #end=time.time()
    #global runtime
    #runtime=end-start
#--------------------------removing border points----------------------------------------------------------------
def ifbordered():
        todel=[]
        if len(coords) != 0:
            for i in range(len(coords)):
                if coords[i][0] == -(sidelength/2):
                    todel.append(coords[i])
                elif coords[i][0] == (sidelength/2):
                    todel.append(coords[i])
                elif coords[i][1] == -(sidelength/2):
                    todel.append(coords[i])
                elif coords[i][1] == (sidelength/2):
                    todel.append(coords[i])
        for elem in todel:
            coords.remove(elem)  
#--------------------execution-----------------------------------------------------------------------------------------
parameters()
