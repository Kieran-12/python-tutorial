import random
import time


def dice(numbers):
    return random.choice(numbers)


dice_sets = {
    "1": [1, 2, 3, 4, 5, 6],
    "2": [1, 1, 1, 7, 8, 8],
    "3": [0, 0, 0, 0, 0, 20],
    "4": [4, 4, 4, 4, 4, 5],
    "5": [1, 1, 1, 1, 5, 6, 6, 7],
}


def computer_roll(dice_choice):
    return dice(dice_sets[dice_choice])


def game():
    print("Welcome to the dice rolling game!")
    print("This game is for 2 players.")

    while True:
        choice = input(
            "Would you like to play with a computer or another player? (1 for computer and 2 for another player) "
        )
        if choice in ("1", "2"):
            break
        else:
            print(
                "Please input a valid response (1 for computer and 2 for another player)"
            )

    if choice == "1":
        player1 = "Computer"
        player2 = "You"
    else:
        player1 = "Player 1"
        player2 = "Player 2"

    while True:
        print("\nSelect a dice set:")
        print("1. Dice Set 1: [1, 2, 3, 4, 5, 6]")
        print("2. Dice Set 2: [1, 1, 1, 7, 8, 8]")
        print("3. Dice Set 3: [0, 0, 0, 0, 0, 20]")
        print("4. Dice Set 4: [4, 4, 4, 4, 4, 5]")
        print("5. Dice Set 5: [1, 1, 1, 1, 5, 6, 6, 7]")
        dice_choice = input("Enter the number of the dice set you want to use: ")

        if dice_choice in dice_sets:
            break
        else:
            print("Invalid choice. Please select a valid dice set.")

    score1 = 0
    score2 = 0

    while True:
        input("\nPress Enter to roll the dice...")
        result1 = (
            computer_roll(dice_choice)
            if player1 == "Computer"
            else dice(dice_sets[dice_choice])
        )
        result2 = (
            computer_roll(dice_choice)
            if player2 == "Computer"
            else dice(dice_sets[dice_choice])
        )

        print("\nLet's roll the dice!")
        print(f"{player1} rolls the dice...")
        time.sleep(1)  # Adding a delay for dramatic effect
        print(f"{player1} rolled: {result1}")
        score1 += result1

        print(f"{player2} rolls the dice...")
        time.sleep(1)  # Adding a delay for dramatic effect
        print(f"{player2} rolled: {result2}")
        score2 += result2

        print(f"\n{player1} score: {score1}")
        print(f"{player2} score: {score2}")

        if score1 >= 50:
            print(f"\n{player1} wins!")
            break
        elif score2 >= 50:
            print(f"\n{player2} wins!")
            break


game()
