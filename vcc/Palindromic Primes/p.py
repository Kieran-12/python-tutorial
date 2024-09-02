# PASTE YOUR check_prime FUNCTION HERE.
def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# PASTE YOUR check_palindrome FUNCTION HERE.
def check_palindrome(number):
    return str(number) == str(number)[::-1]


# TYPE YOUR REMAINING CODE HERE.
for num in range(1, 20001):
    if check_prime(num) and check_palindrome(num):
        print(num)
