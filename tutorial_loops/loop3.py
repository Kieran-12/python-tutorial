for step in range(0, 20):
    print(step)

x = 45
y = 80

while x<50 and y<100:
    x = x+1
    y = y+1
    print(x, y)
    
while x<50 or y<100:
    x = x+1
    y = y+1
    print(x, y)
    
for x in range(0, 20):
    print("hello %s"% x)
    if x >= 9:
        break