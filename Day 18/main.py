from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.pensize(10)
turtle.penup()

def set_color(turtle):
    R = random.random()
    G = random.random()
    B = random.random()
    turtle.color(R,G,B)

def place_dot(turtle):
   set_color(turtle)
   turtle.dot()

def should_turn_left(location):
  if location % 100 == 0 and location != 0 and location % 200 == 0:
   return True
  return False

def turn_left(turtle):
    turtle.left(90)
    turtle.forward(25)
    place_dot(turtle)
    turtle.left(90)

def should_turn_right(location):
   if location %100 == 0 and location != 0 and location %200 != 0:
      return True
   return False

def turn_right(turtle):
    turtle.right(90)
    turtle.forward(25)
    place_dot(turtle)
    turtle.right(90) 

def finish(turtle):
   place_dot(turtle)
   turtle.forward(200) 

for i in range (800):
   if i % 25 == 0:
      place_dot(turtle)
      turtle.forward(1)
   else:
      turtle.forward(1)
   if should_turn_left(i):
      turn_left(turtle)
   elif should_turn_right(i):
      turn_right(turtle)

finish(turtle)
    


   
   
   

  
    
    

  



















screen.exitonclick()
