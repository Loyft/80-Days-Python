import colorgram
import turtle as t
import random

screen = t.Screen()
tim = t.Turtle()
t.colormode(255)
tim.hideturtle()

# Get colors
rgb_colors = []

colors = colorgram.extract('hirst.jpeg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    if r > 220 and g > 220 and b > 220:
        pass
    else:
        rgb_colors.append(rgb)

# Move to start position
tim.penup()
tim.right(180)
tim.forward(225)
tim.left(90)
tim.forward(225)


def draw_dot():
    tim.dot(20, random.choice(rgb_colors))


def move_next_spot():
    tim.setheading(0)
    for _ in range(10):
        draw_dot()
        tim.forward(50)


def move_next_row():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)


for _ in range(10):
    move_next_spot()
    move_next_row()

screen.screensize(400, 400)
screen.exitonclick()
