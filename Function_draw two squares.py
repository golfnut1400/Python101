import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex, 50)          # Calls the function to draw the square

alex.penup()
alex.goto(100,100)             # moves away from the first square
alex.pendown()

drawSquare(alex,75)           # Calls the function then Draws another square

wn.exitonclick()
