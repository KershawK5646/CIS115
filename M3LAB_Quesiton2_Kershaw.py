"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def isosceles(t, r, angle):
    """Draws an Isosceles triangle.

    The turtle will start and end at the peak
    Facing the middle of the base.
    
    t: Turtle
    r: Length of the equal legs
    angle: Peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)
    rt(t, angle)
    fd(t, r)
    lt(t, 90 + angle)
    fd(t, 2 * y)
    lt(t, 90 + angle)
    fd(t, r)
    lt(t, 180 - angle)

def polypie(t, n, r):
    """ Draws a pie divided into radial segments.
    t: Turtle
    n: Number of sides
    r: Length spokes
    """
    angle = 360 / n
    for i in range(n):
        isosceles(t, r, angle / 2)
        lt(t, angle)
    

# the starting point of our program
def main():
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001
    
    # Move the turtle into place
    pu(bob)
    lt(bob, 180)
    fd(bob, 150)
    pd(bob)
    # draw pie 1
    polypie(bob, 5, 50)
    # Move the turtle into place
    pu(bob)
    lt(bob, 180)
    fd(bob, 150)
    pd(bob)
    # draw pie 2
    polypie(bob, 6, 50)
    # Move the turtle into place
    pu(bob)
    fd(bob, 150)
    pd(bob)
    # draw pie 3
    polypie(bob, 7, 50)
    
    wait_for_user()

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    main()
