from turtle import Screen
import time
from snek import Snek
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snejkerkurwa")

screen.tracer(0)
wonsz = Snek()

is_game_on = True
print(wonsz.__dict__)

while is_game_on:
    for _ in range(5):
        wonsz.gosnek()
        time.sleep(0.1)
        wonsz.sneklist[0].forward(20)
        screen.update()
    wonsz.rightsnek()
    wonsz.gosnek()