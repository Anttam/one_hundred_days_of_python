from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while(True):
  drink = input(" What would you like? (espresso, cappuccino, latte): ")
  if drink == 'q' or drink == 'quit':
    break

  if drink == 'report':
    maker.report()
    money.report()
    continue  

  drink = menu.find_drink(drink)

  if not drink:
    continue

  if not maker.is_resource_sufficient(drink):
    continue

  menu.print_price(drink)

  if not money.make_payment(drink.cost):
    continue
  
  maker.make_coffee(drink)