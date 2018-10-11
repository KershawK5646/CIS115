"""
This program draws a pumpkin

    Start with a circle
    Draw two triangles for eyes
    Draw a rectangle for a mouth
"""

import turtle

def drawPumpkin(t):

    #Relocates the turtle without leaving a mark.
    t.speed(50)
    t.penup()
    t.setposition(0, -200)
    t.pendown()

    #Draws the pumpkin body
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(225)
    t.end_fill()
    """
    The following draws the eyes.
    """
    #Relocates the turtle
    t.penup()
    t.setposition(-120, 95)
    t.pendown()
    #Draws the Left eye.
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(3):
        t.forward(75)
        t.left(120)
    t.end_fill()
    #Relocates the turtle
    t.penup()
    t.setposition(45, 95)
    t.pendown()
    #Draws the Right eye.
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(3):
        t.forward(75)
        t.left(120)
    t.end_fill()

    """
    The following draws the mouth
    """
    #Relocates the turtle
    t.penup()
    t.setposition(-135, -100)

    #Draws rectangle for mouth
    t.fillcolor('yellow')
    t.begin_fill()
    t.pendown()
    t.forward(270)
    t.left(90)
    t.forward(65)
    t.left(90)
    t.forward(270)
    t.left(90)
    t.forward(65)
    t.left(90)
    t.end_fill()


def main():
    jason = turtle.Turtle()
    drawPumpkin(jason)

if __name__ == "__main__":
    main()
