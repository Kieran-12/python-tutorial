import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
 
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
random.shuffle(desserts)
print(desserts)