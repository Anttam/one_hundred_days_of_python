import time
from turtle import Screen, Turtle

from midline import MidLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_over = False
screen = Screen()

screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()
midline = MidLine()
left_paddle = Paddle('left')
right_paddle = Paddle('right')
ball = Ball()

screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'i')
screen.onkey(right_paddle.down, 'k')

while not game_over:
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if ball.xcor() < 360 and ball.distance(right_paddle) < 50 or ball.xcor() > -350 and ball.distance(left_paddle) < 50:
    ball.bounce_x()
  
  if ball.xcor() > 380:
    scoreboard.score_left()
    scoreboard.update_score()
    ball.goto(0,0)
    ball.bounce_x()

  if ball.xcor() < -390:
    scoreboard.score_right()
    scoreboard.update_score()
    ball.goto(0,0)
    ball.bounce_x()

  ball.move()
    
  screen.update()
  
screen.exitonclick()