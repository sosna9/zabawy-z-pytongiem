import colorgram
from turtle import *
import random

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 20)
for color in colors:
    r, g, b = color.rgb
    rgb_colors.append((r, g, b))

for popa in range(7):
    rgb_colors.pop(0)

print(rgb_colors)
print(random.choice(rgb_colors))
print(len(rgb_colors))


def randdraw(lil, length):
    for _ in range(length):

        lil.color(random.choice(rgb_colors))
        lil.right((random.randint(-30, 30)))
        lil.forward(random.randint(0, 10))

colormode(255)
timmy = Turtle()
timmy.pensize(5)
timmy.shape("turtle")
screen = Screen()
timmy.speed(0)
print(screen.screensize())
timmy.clear()
timmy.speed(0)
randdraw(timmy, 70)

