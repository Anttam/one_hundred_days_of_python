from turtle import Turtle

class Player(Turtle):
  def __init__(self):
    super().__init__('turtle')
    self.color('green')
    self.penup()
    self.seth(90)
    self.start = (0, -280)
    self.go_to_start()

  def move_forward(self):
    self.forward(20)
  
  def move_backward(self):
    self.backward(20)

  def go_to_start(self):
    self.goto(self.start)   