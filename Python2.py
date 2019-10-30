import math

def areaRectangle(b, h):
    z=b*h
    return z

print("base times height = {}".format(areaRectangle(6, 8)))

aInput = 1
bInput = 6
cInput = 8



def quadraticForumla(a, b, c):
    x = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
    return x

print("first root = {}".format(quadraticForumla(aInput, bInput, cInput)))

def quadraticForumlaNeg(a, b, c):
    x = ((-b-math.sqrt(b**2-4*a*c))/(2*a))
    return x

print("2nd root = {}".format(quadraticForumlaNeg(aInput, bInput, cInput)))


