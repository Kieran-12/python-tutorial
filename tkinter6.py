import tkinter
import time
tk=tkinter.Tk()
canvas = tkinter.Canvas(tk,width=800,height=500)
canvas.pack()
mytriangle=canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.01)
def movingtraingle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        canvas.itemconfig(mytriangle, fill='blue')
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        canvas.itemconfig(mytriangle, fill='red')
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        canvas.itemconfig(mytriangle, fill='green')
    else:
        canvas.move(1, 3, 0)
        canvas.itemconfig(mytriangle, fill='black')
canvas.bind_all('<KeyPress-Up>', movingtraingle)
canvas.bind_all('<KeyPress-Down>', movingtraingle)
canvas.bind_all('<KeyPress-Left>', movingtraingle)
canvas.bind_all('<KeyPress-Right>', movingtraingle)
tk.mainloop()
        
