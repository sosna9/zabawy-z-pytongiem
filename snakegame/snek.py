from turtle import Turtle


class Snek:

    def __init__(self):
        self.sneklist = []
        for wonsz in range(3):
            newwonsz = Turtle()
            newwonsz.penup()
            newwonsz.shape("square")
            newwonsz.color("red")
            newwonsz.setpos(-20 * wonsz, 0)
            self.sneklist.append(newwonsz)

    def gosnek(self):
        for num_seg in range(len(self.sneklist) - 1, 0, -1):
            new_x = self.sneklist[num_seg - 1].xcor()
            new_y = self.sneklist[num_seg - 1].ycor()
            self.sneklist[num_seg].setpos(new_x, new_y)

    def rightsnek(self):
        self.sneklist[0].right(90)

    def leftsnek(self):
        self.sneklist[0].left(90)

