# checks to ensure the number is whole, positive and not letter/symobl etc.
def is_whole(number):
    if number.isdigit() == True:
        return True
    else:
        return False


def is_number(number):
    if number.isnumeric() == True:
        return True
    else:
        return False


def is_positive(number):
    if number >= 1:
        return True
    else:
        return False


# function that converts decimal to binary
def decimal_to_binary(decimal_number):
    try:
        binary_number = ""

        while decimal_number > 0:
            binary_number = str(decimal_number & 1) + binary_number
            decimal_number >>= 1
        return binary_number
    except ValueError:
        print("Number is too big.")


number_base10 = input("Number (positive/whole): ")  # original number in decimal form

# checking
if is_whole(number_base10) == True and is_number(number_base10) == True:
    number_base10 = int(number_base10)
    if is_positive(number_base10) == True:
        number_base2 = decimal_to_binary(number_base10)
    else:
        print("Please input another number. Must be a whole, positive number.")

else:
    print("Please input another number. Must be a whole, positive number.")


# placing each digit of binary number into an array
def binary_in_array(binary_number):
    number = []
    for digit in binary_number:
        digit = int(digit)
        number.append(digit)
    return number


# calling the functions
binary_array = binary_in_array(number_base2)

# arrays and counters
count_of_1 = 0
positions_of_1 = []


# counts the number of 1's (if there are 0 or 1 one's, then the result will always be 0)
for digit in binary_array:
    if digit == 1:
        count_of_1 += 1

# base cases (0/1 1's and determining the index's of the 1's and appending them to the positions_of_1 array)
if count_of_1 <= 1:
    print(0)
elif count_of_1 >= 2:
    for index, value in enumerate(binary_array):
        if value == 1:
            positions_of_1.append(index)

# global value to keep track
global_largest_gap = 0

# comparing each difference to determine the largest by comparing with global
for i in range(len(positions_of_1) - 1):
    current_largest_gap = int(positions_of_1[i + 1]) - (positions_of_1[i])
    if current_largest_gap > global_largest_gap:
        global_largest_gap = current_largest_gap

# will always be 1 larger than true value so subtract 1
print(global_largest_gap - 1)
