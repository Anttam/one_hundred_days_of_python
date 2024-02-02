from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, side):
    super().__init__('square')
    if side == 'left':
      self.goto(-360, 0)
    if side == 'right':
      self.goto(360, 0)
    self.shapesize(stretch_wid=1, stretch_len=5)
    self.color('white')
    self.penup()
    self.setheading(90)
  
  def up(self):
    self.forward(20)
    

  def down(self):
     self.backward(20)