import tkinter

FNT = ("Times New Roman", 30)
def pkey(e):
    cvs.delete("all")
    cvs.create_text(200, 50, text="코드="+str(e.keycode), font=FNT)
    cvs.create_text(200, 150, text="심볼="+e.keysym, font=FNT)

root = tkinter.Tk()
root.title("키 값")
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
root.mainloop()
