import turtle
turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(500)

# for x in range (4):
#     turtle.circle(100)
#     turtle.left(90)

# num = 120
# for x in range(num):
#     turtle.circle(150)
#     turtle.left(360//num)

num = 20
for x in range(num):
    turtle.color("blue")
    turtle.circle(100)
    turtle.color("green")
    turtle.circle(50)
    turtle.left(360//num)

turtle.done()