import random
random_num = random.randint(1, 100)
# print(random_num)

while True:
    guess = input("What is the number (1-100)? ")
    if not guess.isdigit():
        print("Please insert a valid number.")
    else:
        guess = int(guess)
        if guess < random_num:
            print("Higher")
        elif guess > random_num:
            print("Lower")
        else:
            print("Congratulations, you have guessed the correct number!")
            break