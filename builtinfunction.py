# abs()
print(abs(10))

# bool()
print(bool(0))
print(bool(1))
print(bool("a"))

# dir()
print(dir(0))

# help()
help(abs)

# eval()
your_calculation = input("Enter a calculation: ")
print(eval(your_calculation))

# exec()
my_small_program = "print('ham'), print('sandwich')"
exec(my_small_program)

# int()
print(int(123.556))
int('123')

# len()
print(len('this is a test string'))
creature_list = ["unicorn", "cyclops","fairy", "elf", "dragon", "troll"]
print(len(creature_list))

# max() min()
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
print(min(numbers))
strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))
print(min(strings))

# range()
for x in range(0, 5):
    print(x)
count_by_twos = list(range(0, 30, 2))
print(count_by_twos)

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)

# sum()
my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
print(sum(my_list_of_numbers))

# file read and write
test_file = open('test.txt')
text = test_file.read()
print(text)

test_file = open('myfile.txt', 'w')
test_file.write('What is green and loud? A froghorn!')
test_file.close()