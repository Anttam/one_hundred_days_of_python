from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

game_over = False

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')

while not game_over:
  screen.update()
  time.sleep(.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.increase_score()
  
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    game_over = True

  for body in snake.bodies[1:]:
   if snake.head.distance(body) < 10:
      game_over = True

score.game_over()
screen.exitonclick()