def at_goal():
  is_at_goal = True;

def right_is_clear():
  wall_on_right = False
def front_is_clear():
  wall_in_front = False

def move():
  robot_position += 1

def turn_left():
  robot_orientation -= 1

def turn_right():
  turn_left()
  turn_left()
  turn_left()

while(not at_goal()):
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else:
    turn_left()
    if front_is_clear():
      move()


