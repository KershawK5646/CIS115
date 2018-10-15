import turtle
import math

def isosceles(r,angle):
    """ DRAWS AN ISOSCELES TRIANGLE

    The turtle will start and end at the peak
    facing the middle of the base.

    r: Length of the equal legs
    angle: Peak angle in degrees
    """

    # Geometric equation to find the base of the triangles.
    y = r * math.sin(angle * math.pi / 180)

    # Step by step to form the triangle itself.
    turtle.right(angle)
    turtle.forward(r)
    turtle.left(90+angle)
    turtle.forward(2*y) #This line is the base
    turtle.left(90+angle)
    turtle.forward(r)
    turtle.left(180-angle)  #This resets the angle of the turtle


def polypie(n ,r):
    """ DRAWS A PIE DIVIDED INTO RADIAL SEGMENTS
    n: Number of sides
    r: Length of spokes
    """
    angle = 360 / n #"Quantizes" the sides of the circle to make it into points
    for i in range(n): #Loop so the program can do more than one number of sides.
        isosceles(r, angle / 2)
        turtle.left(angle)


def main():
    polypie(5, 100)


# Run the program
main()
