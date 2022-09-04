from turtle import *
from random import *
timmy = Turtle()
timmy.shape("turtle")

screen = Screen()


def draw(lil, sides):
    for _ in range(sides):
        lil.forward(100)
        lil.right(360 / sides)


timmy.clear()
for shape in range(3,10):
    draw(timmy, shape)

"""

for i in range(4):
    timmy.forward(300)
    timmy.right(90)
for i in range(20):
    print(i, "\n")
    if (i) % 2 == 0:
        timmy.pd()
    else:
        timmy.up()
    timmy.forward(20)
    """
screen.exitonclick()
