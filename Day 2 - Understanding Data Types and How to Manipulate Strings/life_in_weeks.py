# Request user input for current age.
age = input("How old are you?: ")

# Calculating the remaining lifespan if we live to 90 years.
remaining_life = 90 - int(age)
remaining_days = 365 * remaining_life
remaining_week = 52 * remaining_life
remaining_month = 12 * remaining_life

# Print the message.
print(f"You have {remaining_days} days, {remaining_week} weeks, and {remaining_month} months left")