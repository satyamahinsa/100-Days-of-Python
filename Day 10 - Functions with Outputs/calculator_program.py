import os
from calculator_art import logo
# Calculator Program

def add(num1, num2):
  """Return addition result of 2 numbers

  Args:
      num1 (int): Take a first number
      num2 (int): Take a second number

  Returns:
      int: Addition result of 2 numbers
  """
  return num1 + num2


def subtract(num1, num2):
  """Return subtraction result of 2 numbers

  Args:
      num1 (int): Take a first number
      num2 (int): Take a second number

  Returns:
      int: Subtraction result of 2 numbers
  """
  return num1 - num2


def multiply(num1, num2):
  """Return multiplication result of 2 numbers

  Args:
      num1 (int): Take a first number
      num2 (int): Take a second number

  Returns:
      int: Multiplication result of 2 numbers
  """
  return num1 * num2


def divide(num1, num2):
  """Return division result of 2 numbers

  Args:
      num1 (int): Take a first number
      num2 (int): Take a second number

  Returns:
      int: Division result of 2 numbers
  """
  return num1 / num2

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    calculate_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
    if calculate_again == "y":
      num1 = answer
    else:
      should_continue = False
      os.system("cls")
      calculator()

calculator()
