import random
random.randint(0, 1)


def flip():
    coin_side = random.randint(0, 1)
    if coin_side == 0:
        print('Heads')
    else:
        print('Tails')


while 1:
    print('wanna toss a coin?')
    if bool(input()) == 1:
        flip()
    else:
        print('shame')
        break
