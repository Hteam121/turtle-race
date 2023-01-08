from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=500)
user_bet = s.textinput(title='Make your bet', prompt='Which turtle is going to win the race?')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for color in colors:
    turtles.append(Turtle(shape='turtle'))
    turtles[len(turtles) - 1].color(color)

yVal = 125
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-230, y=yVal)
    yVal -= 50

flag = False
if user_bet:
    flag = True

while flag:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            flag = False
            win_color = turtle.color()[0]
            if win_color == user_bet:
                print(f"You've won, the winning turtle is {win_color}")
            else:
                print(f"You've lost, the winning turtle is {win_color}")


s.exitonclick()
