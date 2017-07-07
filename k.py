import math

def volume(r):
    v = 4/3 * math.pi * r ** 3
    return(v)

def area(r):
    a = 4 * math.pi * r ** 2

print(volume(10))
