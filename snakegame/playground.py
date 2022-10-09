from turtle import Screen
from turtle import Turtle
FONT = ('Courier', 24, 'normal')
class Playground(Turtle):
    def __init__(self):
        super().__init__()

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("snejkerkurwa")
        self.screen.tracer(0)
        self.hideturtle()
        self.color("white")
    def update(self):
        self.screen.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER KUHWA", align='center', font=FONT)
