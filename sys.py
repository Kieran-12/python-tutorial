import sys
def ageEV():
    print("How old are you?")
    age = int(sys.stdin.readline())
    if age <=15:
        print("You are a child.")
    elif age>15 and age<40:
        print("You are young.")
    else:
        print("You are old.")

ageEV()