from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

paddle = Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(350, 0)
paddle.color("white")


def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)


def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")



while(True):
    screen.update()

screen.exitonclick()