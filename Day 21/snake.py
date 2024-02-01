from turtle import Turtle

class Snake:
  def __init__(self):
    self.bodies = []
    self.create_body()
    self.head = self.bodies[0]
  
  def move(self):
        for i in range(len(self.bodies)-1, 0, -1):
          self.bodies[i].goto(self.bodies[i-1].xcor(), self.bodies[i-1].ycor())
        self.head.forward(20)

  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)  

  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)

  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)
  
  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)

  def add_segment(self, position):
    body = Turtle('square')
    body.color('white')
    body.penup()
    body.setpos(position)
    self.bodies.append(body)
    
  def extend(self):
    self.add_segment(self.bodies[-1].position())

  def create_body(self):
    
    head = Turtle('square')
    head.penup()
    head.color('white')
    self.bodies.append(head)
    for i in range(3):
      self.add_segment(head.position())
      