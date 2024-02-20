money = input("Amount of money: ")
percentage = input("Interest rate (number of percentage): ")
years = input("Number of years: ")

money = float(money) 
interest = int(percentage)/100
years = int(years) 

total = money

for x in range (years):
    total = total+total*interest
print(f"${total}")
