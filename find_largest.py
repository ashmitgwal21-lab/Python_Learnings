grades = [85,95,78,15,88,70]

largest_grade = 0
print("Checking grade...")

for grade in grades:
    if grade > largest_grade:
        largest_grade = grade

print(f"The largest number is {largest_grade}")         