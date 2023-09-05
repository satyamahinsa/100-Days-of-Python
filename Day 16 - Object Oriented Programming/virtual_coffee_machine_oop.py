from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
should_continue = True

while should_continue:
  choice = input(f"What would you like? ({menu.get_items()}): ").lower()
  if choice == "off":
    should_continue = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
  else:
    print("Sorry that item is not available.")
