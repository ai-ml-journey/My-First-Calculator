

print("================================")
print("     STUDENT GRADE CALCULATOR")
print("================================")

# Student details
name = input("Enter Student Name: ")

# Enter marks
subjects = ["English", "Mathematics", "Computer Science", "Physics", "Chemistry"]

total_marks = 0

for subject in subjects:
    while True:
        try:
            marks = float(input(f"Enter marks in {subject} (out of 100): "))

            if 0 <= marks <= 100:
                total_marks += marks
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

# Calculate percentage
percentage = total_marks / len(subjects)

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Display result
print("\n================================")
print("         STUDENT RESULT")
print("================================")

print("Student Name:", name)
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
