# This is a basic program showing the functionality of the turtle module.
# It generates a very pretty spiraling pattern.

import turtle   # import the turtle module so we can draw
import math     # import the math module, we need this for e and pi

t = turtle.Pen()    # set a variable to draw with

t.reset()   # clear the screen just in case of leftovers

x = 0       # set some variables to play with
y = 5
z = 10

while x <= 999:         # the more repeats, the larger the pattern
    t.circle(x,13,2)    # this basically sets up 3 arcs which can be varied
    t.circle(y,17,3)
    t.circle(z,19,5)
    x = x + 1           # increment or decrement the radius of each arc by an interesting value
    y = y / math.e
    z = z / math.pi
