import random

input_name = input("Give me everyone's name, separated by commas.")
collection_name = input_name.split(", ")

name = collection_name[random.randint(0, len(collection_name) - 1)]
print(f"The person who paid the bill: {name}")

# Alternative random selection of data in the list
name = random.choice(collection_name)
print(f"The person who paid the bill: {name}")