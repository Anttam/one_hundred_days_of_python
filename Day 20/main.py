from turtle import Screen, Turtle
import time

from snake import Snake








screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()

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




screen.exitonclick()
