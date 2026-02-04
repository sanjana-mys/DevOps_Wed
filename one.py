# Function to calculate total and average
def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


# Take student details
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

# Take marks of 5 subjects
marks = []

print("Enter marks of 5 subjects:")
for i in range(1, 6):
    m = int(input(f"Subject {i}: "))
    marks.append(m)

# Calculate result
total, average = calculate_result(marks)

# Display result
print("\n----- Student Result -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)

# Grade decision
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
