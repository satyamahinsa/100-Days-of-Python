student_score = input("Enter a list of student scores: ").split()
for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])
print(student_score)

max = 0
for value in student_score:
  if value > max:
    max = value

print(f"Highest score in class: {max}")