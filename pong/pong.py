from turtle import Screen
from paddle import Paddle
from ball import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)
FONT = ('Courier', 24, 'normal')

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.direction_x *= -1

    if ball.xcor() > 380:
        print("punkt")
        ball.direction_x *= -1
        ball.goto(0, 0)
        time.sleep(0.5)
    if ball.xcor() < -380:
        print("punkt2")
        time.sleep(0.5)
        ball.direction_x *= -1
        ball.goto(0, 0)
        time.sleep(0.5)

screen.exitonclick()
print("testt")
