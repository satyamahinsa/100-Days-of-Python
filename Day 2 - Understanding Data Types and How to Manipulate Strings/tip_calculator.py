print("Welcome to the Tip Calculator!")

# Request user input for the total bill.
total_bill = int(input("How much is the total bill?: Rp."))

# Asks for user input for the percentage of tip you want to give.
percentage_tip = int(input("What percentage tip do you want to give? (10, 12, or 15): "))

# Requests user input for the number of people paying the bill + tip.
people = int(input("How many people should pay the bill?:"))

# Calculates the bill payment for each person.
bill_each_person = (total_bill * (1 + percentage_tip / 100)) / people

# Print the calculation result for each person's bill payment.
print(f"Each person should pay: Rp. {round(bill_each_person)}")