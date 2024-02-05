from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self, level):
    super().__init__()
    self.penup()
    self.corner = (-200, 270)
    self.middle = (0,0)
    self.color('white')
    self.hideturtle()
    self.write_level(level)

  def write_level(self, level):
    self.goto(self.corner)
    self.clear()
    self.write(f'Current Level: {level}', align='center', font=('Courier', 20, 'normal'))

  def level_up(self):
    self.goto(self.middle)
    self.write("Level up!", align='center', font=('Courier', 20, 'normal'))

  def game_over(self):
      self.goto(self.middle)
      self.write("GAME OVER", align='center', font=('Courier', 20, 'normal'))