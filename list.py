some_numbers = [1, 2, 5, 10, 20]
some_strings = ["Which", "Witch", "Is", "Which"]

some_strings.append("bear burp") # adds "bear burp" to the end of the list
del some_strings[2] # deletes the index 2 in the list (3rd value) which is "Is"
print(some_strings[2]) # prints the new index 2, which is "Which"
print(some_strings[2:4]) # prints index 2-4 (including 2 excluding 4) so prints index 2 and 3, being "Which" and "bear burp"
print(some_strings) 
print(some_numbers + some_strings) # combines both lists
print(some_numbers * 5) # prints the string 5 times

new_numbers = []
for i in range(len(some_numbers)):
    new_numbers.append(some_numbers[i] * 5)
print(new_numbers)
# individually multiplies each of the numbers in the list by 5 instead of repeating it 5 times



