n = int(input())
str1 = "a"
if n % 2 == False:
    print("Please input an even number.")
elif n <= 0:
    print("Please input a positive number at least 1.")
elif n >= 1000:
    print("Please input a number less than 1000.")
else:
    for i in range(0, n // 2 + 1):
        str1 = "*" * (i * 2 + 1)
        print(str1)
