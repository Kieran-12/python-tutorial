x = input("Number of days: ")
x = int(x)

total = 0
for y in range (x):
    total = total + 20
    total = total + y * 10

print(f"Total coins: {total}")




# 20  20+10    20+10+10  20+10+10+10
#     20       20+10     20+10+10
#              20        20+10
#                        20 
                       