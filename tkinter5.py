import tkinter
tk=tkinter.Tk()
canvas = tkinter.Canvas(tk,width=1000,height=1000)
canvas.pack()
my_image=tkinter.PhotoImage(file='111.gif')
canvas.create_image(0,0,anchor=tkinter.NW,image=my_image)
tk.mainloop()