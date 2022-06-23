import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
t.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_random = (r, g, b)
    return color_random


def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(50)
        t.setheading(t.heading() + size_of_gap)


spirograph(10)

screen = Screen()
screen.exitonclick()
