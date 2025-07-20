# Student Report Card Generator

# Student ka naam input lo
name = input("Enter student's name: ")

# Marks input lo
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Total aur percentage calculate karo
total = maths + science + english
percentage = (total / 300) * 100

# Grade decide karo
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

# Report card print karo
print("\n----- Report Card -----")
print(f"Name: {name}")
print(f"Total Marks: {total} / 300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print("-----------------------")
