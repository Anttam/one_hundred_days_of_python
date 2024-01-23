import random

from game_data import data
from art import logo, vs

game_over = False
score = 0


def get_random():
  return data[random.randint(0, len(data)-1)]

def print_description(letter):
    if letter == a:
      print_letter = 'A'
    else:
      print_letter = 'B'
    print(f"Choice {print_letter}: {letter['name']}, a {letter['description']} from {letter['country']}")

def print_score():
  print(f"Your score: {score}")

def print_game():
  print(logo)
  print_score()
  print_description(a)
  print(vs)
  print_description(b)
  choice = change_choice_to_number(input('Who has more followers? Type "A" or "B": '))
  return choice

def compare_followers(a,b):
  if a['follower_count'] > b['follower_count']:
    return 1
  if a['follower_count'] < b['follower_count']:
    return 2

def change_choice_to_number(choice):
  choice = choice.lower()
  if choice == 'a':
    return 1
  if choice == 'b':
    return 2
  
a = get_random()
b = get_random()
winner = compare_followers(a,b)

while not game_over:
  choice = print_game()
  if choice == winner:
    score += 1
    a = b
    b = get_random()
    winner = compare_followers(a,b)
  else:
    print(f"Game Over. your score: {score}")
    game_over = True