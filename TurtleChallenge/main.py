import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_random = (r, g, b)
    return color_random

direction = [0, 90, 180, 270]

for _ in range(200):
    timmy_the_turtle.speed(0)
    timmy_the_turtle.pensize(5)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(10)
    timmy_the_turtle.setheading(random.choice(direction))

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     timmy_the_turtle.color(random.choice(colors))
#     for side in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

#
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)
#
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
# for _ in range(5):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)
#
# for _ in range(6):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
#
# for _ in range(8):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)
#
# for _ in range(9):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)
#




screen = Screen()
screen.exitonclick()




