import turtle
turtle.bgcolor("black")
turtle.speed(500)
c = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range (1000):
    turtle.color(c[x%6])
    turtle.width(x//100+1)
    turtle.forward(x)
    turtle.right(59)

turtle.done()