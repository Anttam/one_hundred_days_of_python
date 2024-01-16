done = False
bids = []
highest_bid = 0
print("Welcome to the silent auction.")
while(not done):
  done = False
  name = input("What is your name? \n")
  bid = int(input("What is your bid amount?\n"))
  person = {
    "name": name,
    "bid": bid
  }
  bids.append(person)
  more_people = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if(more_people == 'no'):
    done = True

for i,person in enumerate(bids):
  if bids[i]['bid'] > bids[highest_bid]['bid']:
    highest_bid = i

print(f"The winner of the auction is {bids[highest_bid]['name']} with the amount ${bids[highest_bid]['bid']}")
