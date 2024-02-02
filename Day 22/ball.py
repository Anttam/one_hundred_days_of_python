from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__('circle')
    self.color('white')
    self.penup()
    self.x_move = 2
    self.y_move = 2

  
  def move(self):
    self.goto(self.x_move + self.xcor(), self.y_move + self.ycor())
  
  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1