from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("circle")

    def move(self):
        print("exdi")
        new_x = self.xcor() +10
        new_y = self.ycor() +10
        self.goto(new_x, new_y)