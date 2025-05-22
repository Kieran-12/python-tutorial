students = {
    "kieran": ["A01", 6],
    "james": ["A02", 7],
    "will": ["A03", 8],
}

name = input("Student Name: ")


# print(students[student])
# print(students.get(student, "Student not found"))

# print(students.get(student.lower(), "Student not found."))

student = students.get(name.lower().strip())

name = name.strip().capitalize()

if student is None:
    print("Student is not found")
else:
    number, age = student
    print(f"The student name is {name}, number is {number}, and is {age} years old.")


