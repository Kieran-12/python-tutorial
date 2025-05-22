your_height = int(input("How tall are you? "))
if your_height>140:
    print("You must buy an adult ticket.")
elif 120<=your_height<=140:
    print("You must buy a children ticket.")
else:
    print("You don't have to buy a ticket.")