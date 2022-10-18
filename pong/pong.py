from turtle import Screen
from turtle import Turtle
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle(360,0)
l_paddle = Paddle(-360,0)




screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()
print("testt")
