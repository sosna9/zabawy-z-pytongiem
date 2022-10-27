from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("circle")
        self.direction_x = 1
        self.direction_y = 1

    def move(self):
        if self.ycor() > 280:
            self.direction_y = -1
        if self.ycor() < -280:
            self.direction_y = 1
        new_x = self.xcor() + 10 * self.direction_x
        new_y = self.ycor() + 10 * self.direction_y
        self.goto(new_x, new_y)
