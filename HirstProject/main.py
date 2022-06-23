# import colorgram
# import colorgram.colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle,Screen
from random import Random
t = Turtle()
turtle.colormode(255)
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86),
 (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219),
 (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
 (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36),
 (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33),
 (37, 45, 83)]

# random_color = random.choice(color_list)
# print(random_color)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100
t.speed(0)
t.penup()
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_count%10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = Screen()
screen.exitonclick()