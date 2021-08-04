import time
import random
import turtle
import math
current=time.time()
turtle.width(3)

def rangetolist(a,b):
    global listedrange
    listedrange=[]
    x=a
    while x<=b:
        listedrange.append(x)
        x += 1
    global current
    t=int((current%(b-a+1))/2)
    global num
    num = listedrange[t]
    current += math.e*math.pi

    
    
steps=0
while steps<500:
    rangetolist(1,100)
    if num%2==0:
        turtle.left(random.randint(10,90))
        turtle.forward(random.randint(10,50))
        steps +=1
    elif num%3==0:
        turtle.right(random.randint(10,90))
        turtle.forward(random.randint(10,50))
        steps +=1
    elif num%4==0:
        turtle.forward(random.randint(10,50))
        steps +=1
    else:
        turtle.backward(random.randint(10,50))
        steps +=1
  

turtle.done()

