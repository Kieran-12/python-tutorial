import turtle
answer = input("Do you want to draw a circle? (yes/no) ").lower()
if (answer=='yes'):
    print("Start drawing")
    turtle.width(2)
    turtle.circle(100)
    turtle.done()
print("Done")