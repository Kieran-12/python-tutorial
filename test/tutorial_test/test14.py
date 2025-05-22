# calculator without eval
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Please enter a valid number.")
    return x / y

print("Welcome to the basic calcultor!")

while True:
    print("The operations are:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter Number (1, 2, 3, 4, 5): ")

    if  choice in ("1", "2", "3", "4"):
        first = float(input("Input First Number: "))
        second = float(input("Input Second Number: "))
        if choice == "1":
            print(f"Result = {add(first, second)}")
        elif choice == "2":
            print(f"Result = {subtract(first, second)}")
        elif choice == "3":
            print(f"Result = {multiply(first, second)}")
        else:
            result = divide(first, second)
            if result is not None:
                print(f"Result = {result}")
    elif choice == "5":
        print("Thanks you for using the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please input a valid number (1, 2, 3, 4, 5)")

            


