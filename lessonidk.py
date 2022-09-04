from turtle import *

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()

for i in range(4):
    timmy.forward(300)
    timmy.right(90)

screen.exitonclick()