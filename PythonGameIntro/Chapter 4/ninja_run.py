import tkinter

scene = "타이틀"
ninja_x = 0
ninja_a = 0

def pkey(e):
    global scene
    if e.keysym=="space":
        scene = "게임"
    if e.keysym=="Return":
        scene = "타이틀"

def main():
    global ninja_x, ninja_a
    cvs.delete("all")
    cvs.create_image(480, 320, image=bg)
    if scene=="타이틀":
        cvs.create_image(480, 320, image=ilst)
        cvs.create_text(480, 180, text="N i n j a r u n", font=("System",100), fill="lime")
        cvs.create_text(480, 420, text="press [SPACE] key", font=("System",40), fill="cyan")
    if scene=="게임":
        ninja_x = ninja_x + 40
        if ninja_x>960: ninja_x = 0
        ninja_a = ninja_a + 1
        cvs.create_image(ninja_x, 400, image=ninja[ninja_a%4])
    root.after(100, main)

root = tkinter.Tk()
root.bind("<Key>", pkey)
cvs = tkinter.Canvas(width=960, height=640)
cvs.pack()
ilst = tkinter.PhotoImage(file="image/illust.png")
bg = tkinter.PhotoImage(file="image/bg.png")
ninja = [
    tkinter.PhotoImage(file="image/ninja0.png"),
    tkinter.PhotoImage(file="image/ninja1.png"),
    tkinter.PhotoImage(file="image/ninja2.png"),
    tkinter.PhotoImage(file="image/ninja3.png")
]
main()
root.mainloop()
