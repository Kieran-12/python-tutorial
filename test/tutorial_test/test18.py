import random
import time


def dice(numbers):
    return random.choice(numbers)


dice_sets = {
    "1": [1, 2, 3, 4, 5, 6],
    "2": [1, 1, 1, 6, 7, 8],
    "3": [0, 0, 0, 0, 0, 25],
    "4": [4, 4, 4, 4, 4, 6],
    "5": [1, 1, 1, 1, 5, 6, 7, 8],
    "6": [1, 3, 6],
}


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
        player1 = "You"
        player2 = "Computer"

    else:
        player1 = "Player 1"
        player2 = "Player 2"


game()
