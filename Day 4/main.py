import random
choices = {
  0 : "Rock",
  1 : "Paper",
  2 : "Scissors"
}
win = "Congragulations you won!"
lose = "The computer won this time"
draw = "You both choose the same! It's a draw"
print("Welcome to Rock Paper Scissors.")

user_choice = choices[int(input("Which do you choose? \nEnter 0 for rock, 1 for paper, and 2 for scissors\n"))]
computer_choice = choices[random.randint(0, 2)]

print(f"you chose: {user_choice}")
print(f"The computer chose: {computer_choice}")

if user_choice == choices[0] and computer_choice == choices[2]:
    print(win)
elif user_choice == choices[1] and computer_choice == choices[0]:
    print(win)
elif user_choice == choices[2] and computer_choice == choices[1]:
    print(win)
elif user_choice == computer_choice:
    print(draw)
else:
    print(lose)