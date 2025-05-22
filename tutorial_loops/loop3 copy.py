import turtle
turtle.bgcolor("black")
turtle.speed(500)
turtle.up()
sides = int(turtle.numinput("Sides", "How many sides? (2-6)",4,2,6))
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for m in range(500):
    turtle.forward(m*4)
    turtle.width(m//24)
    position = turtle.position()
    heading = turtle.heading()
    
    for n in range(int(m/2)):
        turtle.down()
        turtle.color(colors[n%sides])
        turtle.forward(2*n)
        turtle.right(360/sides-2)
        turtle.up()
    
    turtle.setx(position[0])
    turtle.sety(position[1])
    turtle.setheading(heading)
    turtle.left(360/sides+2)

turtle.done()


