import turtle
turtle.bgcolor("black")
t=turtle.Pen()

colors = ["red","yellow","blue","green","orange","purple","white","pink"]
family = []
name=turtle.textinput("My family","Input your family name")

while (name != ""):
    family.append(name)
    name=turtle.textinput("My family","Input your family name")

for x in range(100):
    t.pencolor(colors[x % len(family)])
    t.up()
    t.forward(x * 4)
    t.down()
    t.write(family[x % len(family)], font=("times", int(x+4)//4, "bold"))
    t.left(360 //len(family) + 2)

turtle.done()