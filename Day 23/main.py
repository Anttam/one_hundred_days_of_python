from turtle import Screen
import time

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

game_over = False

current_level = 1
player = Player()
manager = CarManager()
scoreboard = Scoreboard(current_level)

screen.listen()
screen.onkey(player.move_forward, 'w')
screen.onkey(player.move_backward, 's')


manager.start_cars()
while not game_over:

  manager.move_cars()

  for car in manager.cars:
    if player.distance(car) < 25:
      manager.clear_cars()
      scoreboard.game_over()
      screen.update()
      game_over = True
    if car.xcor() <= -350:
      car.hideturtle()
      manager.cars.remove(car)
      manager.create_new_car()

  if player.ycor() >= 270:
    manager.clear_cars()
    scoreboard.level_up()
    screen.update()
    manager.increase_speed()
    manager.start_cars()
    player.go_to_start()
    current_level += 1
    scoreboard.write_level(current_level)
    time.sleep(1)

  screen.update()

screen.exitonclick()