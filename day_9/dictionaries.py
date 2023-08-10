programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

# Retrieving items/value from dictionary.
# print(programming_dictionary["Bug"])

# Adding new items to dictionary.
print("Adding a new item: Loop")
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary.
# programming_dictionary = {}

# Edit an item in a dictionary.
print("Edit a Bug item")
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary.
print("Looping!")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])