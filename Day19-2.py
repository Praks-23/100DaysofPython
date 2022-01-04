from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Betting Center", prompt="Which turtle will you bet on?\nOptions: Red, Yellow, "
                                                           "Blue, Orange, Purple, Green\nEnter a colour : ").lower()
print(f"You've put your bet on {user_bet}.")
r = -100
all_turtles = []
colors = ["red", "yellow", "orange", "purple", "blue", "green"]

for i in range(0, len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=r)
    r += 40
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"!!!🥳Hurray...You have won🥳!!!")
            else:
                print(f"≡(▔﹏▔)≡ You've Lost ≡(▔﹏▔)≡\nThe winning colour is {winning_color}.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
