print("Welcom to the Dice Rolling Simulator!")
import random

while True: 
    roll = random.randint(1, 6)
    print(f"You rolled {roll}.")
    choice = input("Roll Again (yes/no)? ").lower()
    if choice != ("yes"):
        print("Thanks for rolling!")
        break

        

