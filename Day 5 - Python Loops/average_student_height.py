student_height = input("Enter a list of student heights: ").split()

for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
print(student_height)

total_students = 0
total_student_height = 0
for height in student_height:
  total_students += 1
  total_student_height += height

average_student_height = round(total_student_height / total_students)
print(average_student_height)