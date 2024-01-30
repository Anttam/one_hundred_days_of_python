from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
end = False

bet = screen.textinput(title='Make your bet', prompt=' Which turtle do you think will win the race? Enter a color: ')

colors = ['red','orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for i, color in enumerate(colors):
  turtle = Turtle(shape='turtle')
  turtle.color(color)
  turtle.penup()
  turtles.append(turtle)
  if i == 0:
    turtle.goto(-230, -70)
  else:
    turtle.goto(-230,turtles[i-1].ycor() + 30)

while(not end):
  for turtle in turtles:
    turtle.forward(random.randint(0,10))
    if turtle.xcor() >= 230:
      winner = turtle.color()[0]
      end = True

if bet == winner:
  print(f"Congratulations! the {winner} turtle won!")
else:
  print(f"You Lose. the winner was the {winner} turtle")

screen.exitonclick()