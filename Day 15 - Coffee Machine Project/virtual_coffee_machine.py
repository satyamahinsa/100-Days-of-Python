from machine_data import MENU, resources

money = 0

def report_machine(resources, money):
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}ml")
  print(f"Money: ${money}")

def check_resources(order_ingredients):
  global resources
  for item in order_ingredients:
      if resources[item] < order_ingredients[item]:
        print(f"Sorry, there's not enough {item}.")
        return False
  
  return True

def process_coins():
  print("Please insert coins.")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
  return total_money

def make_coffee(order_ingredients, drink_name):
  global resources
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {drink_name}☕. Enjoy!")

def transaction_process(drink_cost, user_money):
  global money
  if user_money == drink_cost:
    money += drink_cost
    return True
  elif user_money > drink_cost:
    print(f"Here is ${round(user_money - drink_cost, 2)} dollars in change.")
    money += drink_cost
    return True
  else:
    print("Sorry, that's not enough money. Money refunded.")
    return False

def coffee_machine():
  should_continue = True

  while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
      should_continue = False
    elif user_input == "report":
      global resources
      report_machine(resources, money)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
      drink = MENU[user_input]
      if check_resources(drink["ingredients"]):
        total_coins = process_coins()
        if transaction_process(drink["cost"], total_coins):
          make_coffee(drink["ingredients"], user_input)
    else:
      print("Invalid input!")

coffee_machine()