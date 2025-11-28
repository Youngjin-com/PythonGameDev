import tkinter
root = tkinter.Tk()
root.title("캔버스에 선을 그어 보자")
cvs = tkinter.Canvas(width=600, height=400, bg="black")
cvs.create_line(0, 0, 580, 380, fill="red", width=5)
cvs.pack()
root.mainloop()
