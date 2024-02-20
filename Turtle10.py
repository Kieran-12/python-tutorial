import turtle
turtle.bgcolor("black")
turtle.speed(100)
colors = ["red", "yellow", "blue", "green", "purple", "white", "pink", "gray"]
num = 160
sides = int(turtle.numinput("Number Of Sides", "How many sides do you want?",4,3,8))
for x in range(100):
    turtle.color(colors[x%sides])
    turtle.forward(x*2)
    turtle.left(360/sides+1)

turtle.done()