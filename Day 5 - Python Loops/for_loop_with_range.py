# Using range() by adding 2 to each element.
# The following loop displays odd numbers between 1-10
for number in range(1, 11, 2):
  print(number)

# Calculates the sum of 1+2+3+4+5+...+98+99+100
total = 0
for number in range(1, 101):
  total += number

print(total)