import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

words = ["grapes", "apples", "bananas", "oranges", "pears"]
word = words[random.randint(0,len(words)-1)]
underscores = ""
current_stage = len(stages) -1
end = False

for letter in word:
  underscores += "_"

print(logo)
print(stages[current_stage])
print(underscores)
while(not end):
  correct_guess = False
  guess = input("Guess a letter: \n")
  for i, letter in enumerate(word):
    if guess == letter:
      underscores = list(underscores)
      underscores[i] = guess
      underscores = ''.join(underscores)
      correct_guess = True
  
  if(not correct_guess):
    current_stage -= 1

  print(stages[current_stage])
  print(underscores)

  if word == underscores:
    print("Congragulations! You guessed the word!")
    end = True
  
  if current_stage == 0:
    print("You lost. Better luck next time.")
    end = True