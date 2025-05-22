import tkinter
tk=tkinter.Tk()
canvas = tkinter.Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_text(150, 150, text='He said,"It\'s my curse,',font=('Times', 15))
canvas.create_text(200, 200, text='but is could be worse,',font=('Helvetica', 20))
canvas.create_text(220, 250, text='my cousin rides round,',font=('Cpurier', 30))
canvas.create_text(220, 300, text='on a goose."',font=('Courier', 30))

tk.mainloop()
