import random, string
letters = ""
symbols = ""
numbers = ""

print("Welcome to the password generator")

num_letters = int(input("How many letters do you want?\n"))
for letter in range(1, num_letters +1):
 letters+= string.ascii_letters[random.randint(0, len(string.ascii_letters) -1)]

num_symbols = int(input("How many special characters do you want?\n"))
for symbol in range(1, num_symbols +1):
 symbols += string.punctuation[random.randint(0,len(string.punctuation) -1)]

num_numbers = int(input("How many numbers do you want?\n"))
for number in range (1, num_numbers +1):
  numbers+= string.digits[random.randint(0, len(string.digits) -1)]

password = list(letters+symbols+numbers)
random.shuffle(password)
password = ''.join(password)

print("Your password is:")
print(password)