print("Welcome to the Love Calculator!")

# Request user input for name1 and name2
# lower() => used to convert all letters in the string to lowercase.
name1 = input("What is your name?: ").lower()
name2 = input("What is your partner's name?: ").lower()

# Declare the variable combined_name to combine name1 and name2.
combined_name = name1 + name2

# Count the number of occurrences of each letter in the word TRUE in both names.
count_t = combined_name.count('t')
count_r = combined_name.count('r')
count_u = combined_name.count('u')
count_e = combined_name.count('e')

# Count the number of occurrences of each letter in the word LOVE in both names.
count_l = combined_name.count('l')
count_o = combined_name.count('o')
count_v = combined_name.count('v')
count_e = combined_name.count('e')

# Calculate the total value of the words TRUE and LOVE.
total_true = count_t + count_r + count_u + count_e
total_love = count_l + count_o + count_v + count_e

total_score = int(str(total_love) + str(total_love))

if total_score < 10 or total_score > 90:
  print(f"The total score is {total_score}, your relationship is like cola and mentos.")
elif total_score > 40 and total_score < 50:
  print(f"Total score is {total_score}, your relationship is good forever.")
else:
  print(f"The total score is {total_score}.")