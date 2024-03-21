from flask import Flask
import random
app = Flask(__name__)

number = random.randint(0,9)

@app.route('/')
def hello_world():
  return '<h1>Guess a number between 0 and 9</h1>'\
          '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'
        
@app.route('/<int:guess>')
def check_guess(guess):
  if guess < number:
        return '<h1>Too low, Try again!</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
  if guess > number:
      return '<h1>Too high, Try again!</h1>' \
          '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
  if guess == number:
    return '<h1>You found me!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
  

if __name__ == '__main__':
  app.run() 