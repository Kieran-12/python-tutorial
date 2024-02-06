age = int(input("How old are you? "))
gender = input("What is your gender? ")
if age >= 10 and age <= 13:
    print("10-13")
    
if age == 10 or age == 11 or age == 12 or age == 13:
    print("10-13")
    
if gender == "female" and (age == 10 or age == 11 or age == 12 or age == 13):
    print("10-13 female") 