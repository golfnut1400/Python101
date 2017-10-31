import turtle

play = turtle.Turtle()
wn = turtle.Screen()



play.color('red','purple')
play.begin_fill()
play.speed(10)
while True:
    play.forward(200)
    play.left(170)
    if abs(play.pos()) < 1:
        break
play.end_fill()
turtle.done

wn.exitonclick()
