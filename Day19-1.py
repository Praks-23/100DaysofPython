'''
Etch-A-Sketch
- Press w to move forward
- Press s to move backwards
- Press a to turn left
- Press d to turn right
- Press c to clear screen
'''


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()
