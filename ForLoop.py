# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)


# draw a triangle
# import turtle
#
# wn = turtle.Screen()
# triangle = turtle.Turtle()
#
# for i in range(3):
#     triangle.forward(100)
#
#     # the angle of each vertice of a regular polygon
#     # is 360 divided by the number of sides
#     norvig.left(360/3)
#
# wn.exitonclick()

()
# draw a square
import turtle

wn = turtle.Screen()
square = turtle.Turtle()

for i in range(4):
    square.forward(100)
    square.left(360/4)

wn.exitonclick()

# draw a hexagon
import turtle

wn = turtle.Screen()
hexagon = turtle.Turtle()

for i in range(6):
    hexagon.forward(100)
    hexagon.left(360/6)

wn.exitonclick()

# draw an octogon
import turtle

wn = turtle.Screen()
octogon = turtle.Turtle()

for i in range(8):
    octogon.forward(75)
    octogon.left(360/8)

wn.exitonclick()


