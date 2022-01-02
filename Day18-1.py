import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
r = 100


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour=(r,g,b)
    return colour


tim.speed("fastest")
for i in range(0, 72):
    tim.color(random_colour())
    tim.circle(r)
    tim.left(5)

screen = t.Screen()
screen.exitonclick()
