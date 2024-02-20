import turtle
turtle.bgcolor("black")
turtle.speed(500)
num = int(turtle.numinput("Number Of Circles", "How many circles?",6,3,30))
for x in range(num):
    turtle.color("red")
    turtle.circle(100)
    turtle.color("yellow")
    turtle.circle(50)
    turtle.left(360//num)
print("End")
turtle.done()