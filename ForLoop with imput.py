
# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)



import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

# turtle will draw the shapes based on the users imput
# number_of_sides = int(input("Enter the number of sides of the shape: "))

# for i in range(number_of_sides):
#     tess.forward(50)
#     tess.left(360/number_of_sides)
#
# wn.exitonclick()

side_color = tess.color()
fill_color = tess.fillcolor()

number_of_sides = int(input("Enter the number of sides of the shape: "))
side_color = str(input("Enter side color: "))
fill_color = str(input("Enter fill color: "))

for i in range(number_of_sides):
    for s in side_color:
        for c in fill_color:
            tess.forward(50)
            tess.left(360/number_of_sides)

wn.exitonclick()
