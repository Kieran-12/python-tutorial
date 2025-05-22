money = input("Amount of money? ")
save_rate = input("Save rate (number of percentage): ")
years = input("Number of years? ")

percentage = int(save_rate)/100
money = float(money)
years = int(years)

total = money
for x in range (years):
    total = total + total*percentage
    print(f"The total money on year {x+1} is {total}")
