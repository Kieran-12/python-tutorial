characters = [
    "Rachel",
    "Jon",
    "Nick",
    "Ashley",
    "Jake",
    "Joshua",
    "Emily",
    "Kyle",
    "Alex",
    "Sarah",
    "Justin",
    "Megan",
]

number_of_characters = len(characters)

# print(f"There are {number_of_characters} total characters.")
print("There are " + str(number_of_characters) + " total characters.")
print("How many guesses will it take to guess your character?")


guesses = 0

while True:
    print("Keep Guessing!")
    for x in characters:
        print(x)
    blue_eyes = input("Do they have blue eyes? (yes/no) ")
    guesses += 1
    if blue_eyes.lower() == "yes":
        characters = ["Nick", "Emily", "Kyle", "Megan"]
        for x in characters:
            print(x)
        blonde_hair = input("Do they have blonde hair? (yes/no) ")
        guesses += 1
        if blonde_hair.lower() == "yes":
            characters = ["Kyle", "Megan"]
            for x in characters:
                print(x)
            gender = input("Are they male? (yes/no) ")
            guesses += 1
            if gender.lower() == "yes":
                print("Your character is Kyle!")
                break
            else:
                print("Your character is Megan!")
                break
        else:
            characters = ["Nick", "Emily"]
            for x in characters:
                print(x)
            white_hair = input("Do they have white hair? (yes/no) ")
            guesses += 1
            if white_hair.lower() == "yes":
                print("Your character is Emily!")
                break
            else:
                print("Your character is Nick!")
                break
    else:
        print("Rachel, Jon, Ashley, Jake, Joshua, Alex, Sarah, Justin")
        starting_letter = input(
            "Does their first name start with the letter 'J' ? (yes/no) "
        )
        guesses += 1
        if starting_letter.lower() == "yes":
            characters = ["Jon", "Jake", "Joshua", "Justin"]
            for x in characters:
                print(x)
            white__hair = input("Do they have white hair? (yes/no) ")
            guesses += 1
            if white__hair.lower() == "yes":
                characters = ["Jon", "Joshua"]
                for x in characters:
                    print(x)
                moustache = input("Do they have a moustache? (yes/no) ")
                guesses += 1
                if moustache.lower() == "yes":
                    print("Your character is Joshua!")
                    break
                else:
                    print("Your character is Jon!")
                    break
            else:
                characters = ["Jake", "Justin"]
                for x in characters:
                    print(x)
                blonde__hair = input("Do they have blonde hair? (yes/no) ")
                guesses += 1
                if blonde__hair == "yes":
                    print("Your character is Jake!")
                    break
                else:
                    print("Your character is Justin!")
                    break
        else:
            characters = ["Rachel, Ashley, Sarah, Alex"]
            for x in characters:
                print(x)
            hat = input("Are they wearing a hat? (yes/no) ")
            guesses += 1
            if hat.lower() == "yes":
                characters = ["Rachel, Ashley"]
                for x in characters:
                    print(x)
                red_hair = input("Do they have red hair? (yes/no) ")
                guesses += 1
                if red_hair.lower() == "yes":
                    print("Your character is Ashley!")
                    break
                else:
                    print("Your character is Rachel!")
                    break

            else:
                print("Sarah, Alex")
                glasses = input("Are they wearing glasses? (yes/no) ")
                guesses += 1
                if glasses.lower() == "yes":
                    print("Your character is Alex!")
                    break
                else:
                    print("Your character is Sarah!")
                    break

print("Congratulations!")
# print(f"It took {guesses} questions to guess your character!")
print("It took " + str(guesses) + " question to guess your character!")

if guesses == 4:
    print("Choose a different character and try to get it in 3 guesses!")
else:
    print("Choose a different character and try to get it in 4 guesses!")
