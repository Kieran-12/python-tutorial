import turtle

r = input("Radius of circle: ")
if r is None:
    print("Invalid radius.")

r = int(r)
c = input("Colour: ").lower()

turtle.fillcolor(c)
turtle.begin_fill()
turtle.speed(100)

turtle.up()
turtle.setpos(0, -r)
turtle.down()

turtle.circle(r)
turtle.end_fill()
turtle.done()