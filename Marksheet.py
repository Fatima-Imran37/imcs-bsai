name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

subjects = ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]
marks = []

for sub in subjects:
    m = float(input(f"Enter marks for {sub} (out of 100): "))
    marks.append(m)

total_marks = sum(marks)
percentage = total_marks / (5 * 100) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if any(m < 40 for m in marks):
    result = "Fail"
else:
    result = "Pass"

print("\n----- STUDENT MARKSHEET -----")
print(f"Name: {name}")
print(f"Roll No: {roll_no}")
for i, sub in enumerate(subjects):
    print(f"{sub}: {marks[i]}")
print(f"Total Marks: {total_marks}/{5*100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
print("------------------------------")