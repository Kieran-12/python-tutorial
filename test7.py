data = {
    "kieran": ["A01", 6],
    "james": ["A02", 7],
    "will": ["A03", 8],
}

print("Old Data:", repr(data))

name = input("Student Name: ")
age = input("Student Age: ")

student = data.get(name.lower().strip())

if student is None:
    print("Student is not found")
else:
    student[1] = age
    print("Student age updated.")
    print("New Data:", repr(data))
