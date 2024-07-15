#Task 2: Calculate the average grade and print it.


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = 0
grades_length=len(grades)
while grades_length>0:
    grades_length-=1
    average+=grades[grades_length]
average/=len(grades)

print(average)
