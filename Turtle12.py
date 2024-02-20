import turtle
turtle.bgcolor("black")
turtle.speed(0)
sides = int(turtle.numinput("Sides", "How many sides?",4,3,8))
name = turtle.textinput("Name", "Please enter your name.")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]
for x in range(100):
    turtle.color(colors[x%sides])
    turtle.up()
    turtle.forward(x*4)
    turtle.down()
    turtle.write(name, font=("calibri",int(x+4)//4, "bold"))
    turtle.left(360/sides+1)
    turtle.width(x*sides//200)

turtle.done()
