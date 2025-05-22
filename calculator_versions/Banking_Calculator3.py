money = input("Initial Money: ")
percentage = input("Interest Rate (%): ")
years = input("Number Of Years: ")

premium = float(money)
interest = float(percentage)/100
time = float(years)

import math
total_money = premium*math.pow(math.e, interest*time)
rounded_total_money = round(total_money, 2)
print(f"Your total money is ${rounded_total_money}")