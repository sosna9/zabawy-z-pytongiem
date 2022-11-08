def rgb(r, g, b):
    def rounded(x):
        return min(255, max(x, 0))
    return f'{rounded(r):02X}{rounded(g):02X}{rounded(b):02X}'


def solution(s):

    n = 3
    if len(s) % 2:
        s += '_'
    s = [s[i:i + n] for i in range(0, len(s), n)]

    print(s)
    return 0
dupa = 'abdcefghijklmnopqrstuvwxyz'


import re
def solution2(s):
    return re.findall("..", s + "_")
print(solution2('fgdsohngd'))



# txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
# txt2 = "My name is {0}, I'm {1}".format("John", 36)
# test = "dupaa"
# txt3 = f'My name is {test:011}, Im {test=} format'
#
# print(txt3)
#
# print(f"never say you can\'t do something")
