# CIS115
# KershawK
# M3T2
# 10/3/18

# Turtle Python Example 2

import turtle

def main():

    #variables
    sides = int(input("Number of sides? "))
    size = int(input("Size of polygon? "))

    alex = turtle.Turtle()
    bob = turtle.Turtle()
    christine = turtle.Turtle()

    
    # Space the tutles
    alex.forward(size)
    bob.forward(size*4)
    christine.forward(size*8)
    alex.penup
    bob.penup
    christine.penup
    
    # Customize the turtles
    alex.pensize(3)
    bob.pensize(4)
    christine.pensize(2)
    alex.pencolor("red")
    bob.pencolor("green")
    christine.pencolor("blue")

    # Draw shapes
    for t in [alex, bob, christine]:
        drawPolygon(t, sides, size)
    

def drawPolygon(t, sides, size):
    """
    uses turtle to draw a n sided polygon.
    input: t - a turtle
        sides - number of sides
        size - length of one side
    """
    
    for side in range(sides):
        t.forward(100)
        t.right (360/sides) #angle depends on polygon


#run Program
main()
