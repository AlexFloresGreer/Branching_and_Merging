import random
import string
import re

#a = ['IwWpAx', 4, 2, 'TYCm', 'mJmtAYm', 'xKpnPcD', 'Gc', 'MKc', 'epub', 'ABxe']

def randomString(val):
    letters = string.letters
    return "".join(random.choice(letters) for i in range(val))
def makeRandom():
    return [random.randint(5,45) if random.randint(0,1) else randomString(random.randint(2,7)) for y in range(10) ]



print makeRandom()

def group_project1():
    for value in makeRandom():
        if isinstance(value, int):
            print value * "@"
        elif value[0].istitle():
            print value[0], len(value)
        else:
            print value[::-1]

group_project1()
