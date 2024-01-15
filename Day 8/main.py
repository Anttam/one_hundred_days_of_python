import string

letters = list(string.ascii_lowercase)

def encrypt(message, shift):
  encrypted = ''
  for letter in message:
    shifted = letters.index(letter) + shift
    if shifted >= len(letters):
      shifted -= len(letters)
      if shifted == None:
        shifted = 0
      print(shifted)
    encrypted += letters[shifted]
  return encrypted

def decrypt(message, shift):
  unencrypted = ''
  for letter in message:
    shifted = letters.index(letter) - shift
    if shifted < 0:
      shifted = len(letters) - (shifted * -1)
    unencrypted += letters[shifted]
  return unencrypted

print("welcome to the Caesar Cipher")
encode = input('Type "encode" to encrypt. Type "decode" to decrypt:\n')
message = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

if encode == "encode":
  message = encrypt(message, shift)
  print(f"Here is your encoded message: {message}")
elif encode == "decode":
  message = decrypt(message, shift)
  print(f"your decoded messge is: {message}")





