import turtle
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]
turtle.speed(0)
sides = 8

for x in range:
    turtle.color(colors[x%sides])
    turtle.forward(x*2)
    turtle.left(360//sides+1)

turtle.done()

