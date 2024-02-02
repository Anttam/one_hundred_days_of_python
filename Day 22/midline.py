from turtle import Turtle

class MidLine:
  def __init__(self):
    self.mid_line = []
    self.create_line()
    

  def create_line(self):
    for i in range(55):
      line = Turtle('square')
      line.color('white')
      line.penup()
      line.shapesize(stretch_len=.5, stretch_wid=.5)
      if i % 3 != 0:
        line.color('white')
      else:
        line.color('black')
      if i == 0:
        line.goto(0,275)
      else:
        line.goto(0, self.mid_line[i-1].ycor() - 10)
      self.mid_line.append(line)