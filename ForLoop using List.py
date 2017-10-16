#
# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps,
# turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken.
# Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.
#


import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

# lift pen and move forward so steps are drawn in window
lovelace.penup()
lovelace.forward(100)

# list of angles used by the pirate
angle = [160, -43, 270, -97, -43, 200, -940, 17, -86]

lovelace.pendown()
for index in angle:

    # we use .left() so that positive angles are counter-clockwise
    # and negative angles are clockwise
    lovelace.left(index)
    lovelace.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", lovelace.heading())

wn.exitonclick()
