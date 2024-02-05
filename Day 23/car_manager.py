from turtle import Turtle
import random

class CarManager:
  def __init__(self):
    self.colors = ['red', 'blue', 'yellow', 'orange', 'purple']
    self.cars = []
    self.speed = .4

  def create_car(self, start_x, start_y):
    car = Turtle('square')
    car.shapesize(stretch_wid=1, stretch_len=2)
    car.penup()
    car.color(random.choice(self.colors))
    car.seth(180)
    car.goto(start_x, start_y)
    self.cars.append(car)

  def start_cars(self):
    for _ in range(40):
      self.create_car(random.randint(-260,300), random.randint(-220, 240))

  def create_new_car(self):
    self.create_car(300, random.randint(-220, 240))

  def move_cars(self):
    for car in self.cars:
      car.forward(self.speed)

  def clear_cars(self):
    for car in self.cars:
      car.hideturtle()
    self.cars.clear()

  def increase_speed(self):
    self.speed += .1