from turtle import *

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()


for i in range(4):
    timmy.forward(300)
    timmy.right(90)
timmy.clear()
for i in range(20):
    print(i, "\n")
    if (i) % 2 == 0:
        timmy.pd()
    else:
        timmy.up()
    timmy.forward(20)
screen.exitonclick()