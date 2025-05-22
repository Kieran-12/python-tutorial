def solution(N):

    def decimal_to_binary(decimal_number):
        try:
            binary_number = ""

            while decimal_number > 0:
                binary_number = str(decimal_number & 1) + binary_number
                decimal_number >>= 1
            return binary_number
        except ValueError:
            print("Number is too big.")

    number_base2 = decimal_to_binary(N)

    def binary_in_array(binary_number):
        number = []
        for digit in binary_number:
            digit = int(digit)
            number.append(digit)
        return number

    binary_array = binary_in_array(number_base2)

    count_of_1 = 0
    positions_of_1 = []

    for digit in binary_array:
        if digit == 1:
            count_of_1 += 1

    global_largest_gap = 0
    if count_of_1 <= 1:
        print(0)
    elif count_of_1 >= 2:
        for index, value in enumerate(binary_array):
            if value == 1:
                positions_of_1.append(index)

        for i in range(len(positions_of_1) - 1):
            current_largest_gap = int(positions_of_1[i + 1]) - (positions_of_1[i])
            if current_largest_gap > global_largest_gap:
                global_largest_gap = current_largest_gap

        print(global_largest_gap - 1)


if __name__ == "__main__":
    N = int(input("give number: "))
    solution(N)
