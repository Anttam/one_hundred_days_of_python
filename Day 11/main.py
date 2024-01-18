import random
from art import logo
cards = [11, 2, 3,4,5,6,7,8,9,10,10,10,10]
stop_playing = False

def start_hand ():
  hand = []
  for card in range(0,2):
    hand.append(cards[random.randint(0,len(cards)-1)])
  return hand

def add_card():
  return cards[random.randint(0,len(cards)-1)]

def total_hand(hand):
  return sum(hand)

def check_for_aces(hand):
  total = sum(hand)
  for i, card in enumerate(hand):
    if total > 21:
      if card == 11:
        total -= 10
        hand[i] = 1  
  return hand

def determine_winner(player_total, op_total):
  if op_total > player_total and op_total <= 21:
    return'You Lose!'
  elif op_total < player_total or op_total > 21:
    return 'You Win!'
  elif op_total == player_total:
    return 'Draw!'



def game(player, op):
  end = False 
  player_total = total_hand(player)
  op_total = total_hand(op)
  while(not end):
    print(f"\nYour cards: {player} Total: {player_total}")
    print(f"\nComputer's first card: {op[0]}")
    hit = input("\nType 'h' to hit or 's' to stand\n")

    if hit == 'h':
      player.append(add_card())
      player = check_for_aces(player)
      player_total = total_hand(player)
      if player_total > 21:
          print(f"\nYour Hand: {player} Total: {player_total}")
          print("\nbust")
          end = True

    if hit == 's':
      while(op_total < 18):
        op.append(add_card())
        op = check_for_aces(op)
        op_total = total_hand(op)
      print(f"\nYour Hand: {player} Total: {player_total}")
      print(f"\nComputer's Hand: {op} Computer's Total:{op_total}")
      print(determine_winner(player_total, op_total))
      end = True

while(not stop_playing):
  player = check_for_aces(start_hand())
  op = start_hand()
  game(player, op)
  keep_playing = input("Would you like to play again? Type 'y' for yes and 'n' for no.")
  if keep_playing == 'n':
    stop_playing = True
  print('____________________________________________')
  player.clear()
  op.clear()