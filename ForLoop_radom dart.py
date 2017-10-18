
import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

fred.up()

numdarts = 10
for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x = randx
    y = randy

    print (x)
    print (y)
    fred.goto(x,y)  # use of 'goto() function to move the random postion
    fred.down()
    fred.dot(10, "red")

print("done")

wn.exitonclick()
