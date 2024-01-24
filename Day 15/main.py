from data import MENU, resources, coins

def print_report():
  dollar_sign = ''
  for resource, amount in resources.items():
    if resource == 'coffee':
      measure = 'g'
    elif resource == 'money':
      dollar_sign = '$'
      measure = ''
      amount = "{0:.2f}".format(amount)
    else:
      measure = 'ml'
    print(f'{resource} : {dollar_sign}{amount}{measure}')

def print_cost(drink):
  print(f'The price is ${"{0:.2f}".format(drink["cost"])}. Please insert coins.')

def check_resources(drink):
  drink_requirements = drink['ingredients']
  for requirement in drink_requirements:
    if drink_requirements[requirement] > resources[requirement]:
      return False
  return True

def request_payment():
  totals = {}
  amount = 0
  for coin in coins:
    total = int(input(f"how many {coin}s? "))
    totals[coin] = total
  for coin in totals:
    amount += (totals[coin] * coins[coin])
  totals['total'] = amount
  return totals

def payment_amount_enough(drink,totals):
  if totals['total'] >= drink['cost']:
    return True
  else:
    return False
  
def enough_resources(requested_drink):
  ingredients = requested_drink['ingredients']
  for requirement in ingredients:
    if resources[requirement] < ingredients[requirement]:
      return False
  return True

def make_drink(requested_drink):
  global resources
  ingredients = requested_drink['ingredients']
  for ingredient in ingredients:
    resources[ingredient] -= ingredients[ingredient]

def collect_payment(totals):
  resources['money'] += totals['total']
  
def give_change(totals, requested_drink):
  change_due = totals['total'] - requested_drink['cost']
  resources['money'] -= change_due
  print(f' Your change is ${"{0:.2f}".format(change_due)}')

def not_enough_resource(drink):
  ingredients = drink['ingredients']
  for resource in ingredients:
    if resources[resource] <= ingredients[resource]:
      print(f"There is not enough {resource}")

def not_enough_money(drink):
  print(f'you do not have enough money for a {drink}')

def need_change(totals, requested_drink):
  if totals['total'] > requested_drink['cost']:
    return True
  else:
    return False
  
def serve(drink):
  print(f"here is your {drink}")



while True:
  drink = input(" What would you like? (espresso, cappuccino, latte): ")
  if drink == 'report':
    print_report()
  elif drink == 'q':
    break 
  else:
    requested_drink = MENU[drink]
    if enough_resources(requested_drink):
      print_cost(requested_drink)
      totals = request_payment()
      if payment_amount_enough(requested_drink, totals):
          make_drink(requested_drink)
          collect_payment(totals)
          if need_change(totals, requested_drink):
            give_change(totals, requested_drink)
          serve(drink)
      else:
        not_enough_money(drink)
    else:
      not_enough_resource(requested_drink)
  print('__________________________\n')