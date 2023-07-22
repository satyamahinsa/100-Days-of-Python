# Functions with multiple return values
def format_name(first_name, last_name):
  if first_name == "" or last_name == "":
    return "Invalid Input!"
  return f"{first_name.title()} {last_name.title()}"

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))