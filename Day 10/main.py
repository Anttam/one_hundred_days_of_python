from art import logo
done = False
skip_first = False

def add(first, second):
  return first + second
def subtract(first, second):
  return first - second
def multiply(first, second):
  return first * second
def divide(first,second):
  if second == 0:
    return 
  return first / second
def print_operations():
  print('+ \n - \n * \n / \n')

print(logo)
while(not done):
  if not skip_first:
    first = int(input("What is the first number?: "))
  print_operations()
  operation = input("Pick an operation: ")
  second = int(input("What is the next number?: "))

  if operation == "+":
    answer = add(first, second)
  elif operation == "-":
    answer = subtract(first, second)
  elif operation == '*':
    answer = multiply(first, second)
  elif operation == '/':
    answer = divide(first, second)
    answer = round(answer, 2)

  print(f"{first} {operation} {second} = {answer}")
  
  next = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. Type 'q' to quit: \n")

  if next == 'y':
    first = answer
    skip_first = True
  elif next == 'n':
    skip_first = False
  elif next == 'q':
    done = True


  

