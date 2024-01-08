print("Welcome to Treasure Island \nTry to make your way to the treasure!")
direction = input("You are at a crossroad. Will you go left or right?\n")
if direction.lower() == "left":
  is_waiting = input('You come to a lake. Type "wait" to wait for a boat. Type "swim" to swim across\n')
  if is_waiting.lower() == "wait":
    door = input("You arrive at the island unharmed. \nThere is a house with 3 doors. One red, one blue, and one yellow. Which color will you choose?\n")
    door = door.lower()
    if door == "yellow":
      print("Congratulations! you found the treassure!")
    elif door == "blue":
      print("You open the door to a hungry lion. \nGame Over")
    else:
      print("the door opens to a room full of flames. \nGame Over")
  else:
    print("You get a quarter of a mile across the lake and remember you ate 20 minutes ago. You cramp up and drown. \nGame Over")
else:
  print("you make a left and trip over a rock, knocking you unconcious. \nGame Over")

