from turtle import Turtle
import time

MOV_DIST = 20
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180


class Snek:

    def __init__(self):
        self.sneklist = []
        for wonsz in range(7):
            newwonsz = Turtle()
            newwonsz.penup()
            newwonsz.shape("square")
            newwonsz.color("blue")
            newwonsz.setpos(-20 * wonsz, 0)
            self.sneklist.append(newwonsz)
        self.head = self. sneklist[0]

    def extend(self):
        self.add_segment(self.sneklist[-1].position())
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.sneklist.append(new_segment)
    def gosnek(self):
        for num_seg in range(len(self.sneklist) - 1, 0, -1):
            new_x = self.sneklist[num_seg - 1].xcor()
            new_y = self.sneklist[num_seg - 1].ycor()
            self.sneklist[num_seg].setpos(new_x, new_y)
        time.sleep(0.1)
        self.sneklist[0].forward(MOV_DIST)

    def rightsnek(self):
        if self.sneklist[0].heading() != LEFT:
            self.sneklist[0].setheading(RIGHT)

    def leftsnek(self):
        if self.sneklist[0].heading() != RIGHT:
            self.sneklist[0].setheading(LEFT)

    def downsnek(self):
        if self.sneklist[0].heading() != UP:
            self.sneklist[0].setheading(DOWN)

    def upsnek(self):
        if self.sneklist[0].heading() != DOWN:
            self.sneklist[0].setheading(UP)
