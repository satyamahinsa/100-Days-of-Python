# Review
def greet():
    print("Hello")
    print("Success call greet()")
    print("Bye")

greet()

# Function that allows for input.
# Parameter => name of the data and use to refer the data and to do things with it.
def greet(name):
    print(f"Hello {name}")
    print("Success call greet()")
    print(f"Bye {name}")

# Argument => actual piece of data 
# that's going to be passed over to the function when it's being called.
greet("Satya")