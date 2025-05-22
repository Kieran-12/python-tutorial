import tkinter
tk=tkinter.Tk()
canvas = tkinter.Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_polygon(1,1,100,10,100,110,fill="",outline="black")
canvas.create_polygon(200,10,240,30,120,100,140,120,fill="",outline="black")
tk.mainloop()