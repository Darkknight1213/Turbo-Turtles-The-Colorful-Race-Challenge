from turtle import *
import random
is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter a color: ")
color = ["red", "blue", "orange", "purple", "green", "yellow"]
turtles = []

a = 125
for i in color:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(-240, a)
    turtles.append(tim)
    a -= 50
til = Turtle(shape="turtle")
til.hideturtle()
til.goto(0,0)

while is_race_on:
    for i in turtles:
        i.speed("fastest")
        if i.xcor() > 200:
            is_race_on = False
            winn = i.pencolor()
            if winn == user_bet:
                print("you won, {}".format(winn))
                til.write(f"Congratulations {winn} won", align="center", font=("Arial", 20, "normal"))
            else:
                print("you lost to {}".format(winn))
                til.write(f"{winn} won, Better luck next time", align="center", font=("Arial", 20, "normal"))
        randdis = random.randint(0, 30)
        i.forward(randdis)



screen.mainloop()