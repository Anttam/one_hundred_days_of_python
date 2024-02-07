import pandas, turtle

screen = turtle.Screen()
screen.title("US States Game")
image = 'Day 25/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
  guess = screen.textinput(title='Guess the state', prompt="What is the state's name?").title().goto(-500,500)
  data = pandas.read_csv('Day 25/50_states.csv')

  state_list = data.state.to_list()

  if guess in state_list:
    guessed_states.append(guess)
    state_data = data[data.state == guess]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(state_data.x), int(state_data.y))
    t.write(guess)

screen.exitonclick()

