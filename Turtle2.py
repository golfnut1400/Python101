import turtle

play = turtle.Turtle()
wn = turtle.Screen()


play.hideturtle()
play.speed(25)
play.color("orange")
play.pensize(1)

for i in range(100):
    play.forward(i)
    play.right(100)
    play.radians()

wn.exitonclick()
