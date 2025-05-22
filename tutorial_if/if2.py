driving_age = int(input("What is the legal driving age? "))
your_age = int(input("How old are you? "))
if your_age>driving_age:
    print("You are old enough to drive.")
if your_age<driving_age:
    years = driving_age - your_age
    print(f"You still have to wait {years} more year(s) to drive.")