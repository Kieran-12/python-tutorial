myval = None
if myval == None:
    print("The variable myval doesn't have a value.")
    
age = 10
if age == 10:
    print("The variable myval doesn't have a value.")

age = "10"
if age == 10:
    print("The variable myval doesn't have a value.")
else:
    print("The variable myval has a value.")

age = "10"
converted_age = int(age)
age = 10
conversion = str(age)
age = "10.5"
convert = float(age)

print(converted_age)
print(conversion)
print(convert)

