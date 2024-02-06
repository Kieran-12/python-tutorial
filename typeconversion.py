myval = None
if myval == None:
    print("The variable myval doesn't have a value")

age = 10 
if age == 10:
    print("The variable myval doesn't have a value")
    
age = "10"
converted_age = int(age)
age = 10
converted_age = str(age)
age = "10.5"
converted_age = float(age)
print(converted_age)