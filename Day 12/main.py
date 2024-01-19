import random

number = random.randint(1,100)
guesses = 0

def set_difficulty(choice):
  if choice == 'easy':
    return 10
  if choice == 'hard':
    return 5
def print_remaining():
  print(f'You have {guesses} attempts remaining to gues the number')
def ask_for_number():
  return int(input('Make a guess: '))
def check_higher_lower(guess):
  if number > guess:
    return 'Too Low'
  elif number < guess:
    return 'Too High'
  elif number == guess:
    return 'win'
def print_win():
  print(f'It was {number}! You guessed the right number!')
def print_lose():
  print(f'You lose. the number was {number}')

print('Welcome to the Number Guessing Game')
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')

guesses = set_difficulty(difficulty)

print_remaining()
guess = ask_for_number()

while(guesses > 1 ):
  check = check_higher_lower(guess)
  if check == 'win':
    print_win()
    break
  else:
    guesses -= 1
    print(check)
  print_remaining()
  guess = ask_for_number()

if guesses <=1:
  print_lose()