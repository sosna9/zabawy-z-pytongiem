from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x,y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)
        self.color("white")

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)