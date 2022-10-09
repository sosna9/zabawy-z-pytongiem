from turtle import Turtle
import random

class Food(Turtle):

        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color("blue")
            self.speed("fastest")
            self.refresh()
        def refresh(self):
            random_x = 20 * random.randint(-10,10)
            random_y = 20 * random.randint(-10, 10)
            self.goto(random_x, random_y)