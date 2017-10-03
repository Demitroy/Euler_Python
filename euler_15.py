# How many routes from top left corner to bottom right corner in a 20x20 box, moving only down and right.

import time
t1 = time.time()

def factorial(x):
    for i in range(1,x):
        x = x*(i)
    return x

width = 20
height = 20
count = 0

routes = factorial(width+height)/(factorial(width) * factorial(height))
print(routes)
print(time.time() - t1)
