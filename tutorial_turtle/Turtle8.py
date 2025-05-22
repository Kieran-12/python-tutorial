import turtle
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue"]
turtle.speed(500)

for x in range (500):
    turtle.color(colors[x%5])
    turtle.forward(x*2)
    turtle.left(73)

turtle.done()