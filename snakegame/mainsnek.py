from snek import Snek
from playground import Playground
from foood import Food
import time
plansza = Playground()
wonsz = Snek()
food = Food()
is_game_on = True
print(wonsz.__dict__)
plansza.screen.listen()
plansza.screen.onkey(wonsz.upsnek, "Up")
plansza.screen.onkey(wonsz.downsnek, "Down")
plansza.screen.onkey(wonsz.rightsnek, "Right")
plansza.screen.onkey(wonsz.leftsnek, "Left")


while is_game_on:
    wonsz.gosnek()
    plansza.update()
    if wonsz.head.distance(food) < 10:
        food.refresh()
        wonsz.extend()

    if wonsz.head.xcor() > 280 or wonsz.head.xcor() < -280 or wonsz.head.ycor() < -280 or wonsz.head.ycor() > 280:
        print('dupa')
        plansza.game_over()
        plansza.update()
        time.sleep(1)
        is_game_on = False
    for segments in wonsz.sneklist[1::]:
        if wonsz.head.distance(segments) < 10:
            plansza.game_over()
            time.sleep(1)
            is_game_on = False