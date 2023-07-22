# Docstrings
def format_name(first_name, last_name):
  """Format first and last name in title case version"

  Args:
      first_name (string): Take first name
      last_name (string): Take last name

  Returns:
      string: The title case version of the name
  """
  if first_name == "" or last_name == "":
    return "Invalid Input!"
  return f"{first_name.title()} {last_name.title()}"

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))