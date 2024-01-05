bill = float(input("What was the total of the bill?\n"))
people = int(input("How many people to split the bill>\n"))
percent = float(input("What percentage tip would you like to give "))/ 100
tip = bill * percent
total = bill + tip
split = "{:.2f}".format(round(total / people, 2))
print(f"The total each person should pay is ${split}")