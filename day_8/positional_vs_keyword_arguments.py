# Function with more than 1 input.
def greet(name, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")
    print("Success call greet()")
    print(f"Bye {name}")

# Positional Arguments => default way
# Not specified which particular parameter we want to associate,
# just looked at the position.
greet("Satya", 19)

# Keyword Arguments => add each of the parameter names and equal sign with argument
# Argument will associated with parameter
greet(age=19, name="Satya")