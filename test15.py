print("Hello, welcome to the rock, paper, scissors simulator!")

while True:
    import random
    number = random.randint(1, 3)

    if number == 1:
        comp = "rock"
    elif number == 2:
        comp = "paper"
    else:
        comp = "scissors"

    while True:
        choice = input("Choose rock, paper or scissors: ").lower()
        if choice in ("rock", "paper", "scissors"):
            break
        else:
            print("Please input a valid option (Rock, Paper or Scissors).")
    
    if comp == "rock":
        print("Computer chose rock!")
        if choice == "rock":
            print("It's a draw!")
        elif choice == "paper":
            print("You win!")
        else:
            print("You lose! Try again!")
        
    elif comp == "paper":
        print("Computer chose paper!")
        if choice == "rock":
            print("You lose! Try again!")
        elif choice == "paper":
            print("It's a draw!")
        else:
            print("You win!")
    
    else:
        print("Computer chose scissors!")
        if choice == "rock":
            print("You win!")
        elif choice == "paper":
            print("You lose! Try again!")
        else:
            print("It's a draw!")
    
    while True:
        retry = input("Try again? (Yes/No): ").lower()
        if retry not in ("yes", "no"):
            print("Please enter a valid option (Yes/No).")
        else:
            break
    
    if retry == "yes":
        continue
    else:
        break

print("Thanks for playing!")        

