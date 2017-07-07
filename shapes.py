from turtle import *
import math


# Name your Turtle.
crush = Turtle()
color=input("What color would you like?")
sides=input("How many sides do you want")
steps=input("How big would you like the shape?")
# Set Up your screen and starting position.
setup(500,300)
xpos = 0
ypos = 0
crush.setposition(xpos, ypos)

### Write your code below:
crush.pencolor(color)
crush.pendown()

def turtle(steps, sides):
    crush.begin_fill()
    crush.fillcolor(color)
    for shape in range(int(sides)):
        crush.forward(int(steps))
        crush.left(360/int(sides))
    crush.end_fill()
turtle(steps, sides)
exitonclick()
