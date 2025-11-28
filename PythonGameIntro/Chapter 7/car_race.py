import tkinter
import random

WIDTH, HEIGHT = 480, 720
bg_y = 0
pl_x = 0
pl_y = 0
COM_MAX = 10
com_x = [0]*COM_MAX
com_y = [0]*COM_MAX
scene = "타이틀"
score = 0
hisco = 5000

def set_car(): # 차의 초기 좌표를 대입
    global pl_x, pl_y
    pl_x = int(WIDTH/2)
    pl_y = int(HEIGHT/2)
    for i in range(COM_MAX):
        com_x[i] = 172+46*(i%4)
        com_y[i] = 560+60*int(i/4)

def move(e): # 마우스를 움직였을 때
    global pl_x, pl_y
    if scene=="게임":
        pl_x = int(0.8*pl_x+0.2*e.x)
        pl_y = int(0.8*pl_y+0.2*e.y)
        if pl_x<160: pl_x = 160
        if pl_x>320: pl_x = 320

def click(e): # 클릭했을 때
    global scene, score
    if scene=="타이틀":
        scene = "게임"
        score = 0
    if scene=="게임 오버":
        set_car()
        scene = "타이틀"

def text(x, y, txt, siz, col): # 그림자 효과를 준 문자 표시
    fnt = ("Times New Roman", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main(): # 메인 처리를 담당하는 함수
    global bg_y, scene, score, hisco
    cvs.delete("all")
    cvs.create_image(240, bg_y-360, image=bg)
    cvs.create_image(240, bg_y+360, image=bg)
    cvs.create_image(pl_x, pl_y, image=mycar)

    for i in range(COM_MAX): # 적의 차를 담당하는 함수
        if scene=="게임":
            com_y[i] = com_y[i] + 5 + i%5
            if com_y[i]>HEIGHT+40:
                com_x[i] = random.randint(160, 320)
                com_y[i] = -60*i
            dx = abs(com_x[i]-pl_x)
            dy = abs(com_y[i]-pl_y)
            if dx<26 and dy<44:
                scene = "게임 오버"
        cvs.create_image(com_x[i], com_y[i], image=comcar)

    if scene=="타이틀":
        text(240, 240, "Car Race", 60, "red")
        text(240, 480, "Click to start.", 28, "lime")
        bg_y = (bg_y + 2)%HEIGHT

    if scene=="게임":
        score += 10
        if score>hisco: hisco = score
        bg_y = (bg_y + 30)%HEIGHT

    if scene=="게임 오버":
        cvs.create_image(pl_x, pl_y, image=mycar2)
        text(240, 320, "GAME OVER", 40, "red")

    text(120, 20, "SCORE "+str(score), 24, "cyan")
    text(360, 20, "HI "+str(hisco), 24, "yellow")
    root.after(33, main)

root = tkinter.Tk()
root.title("Car Race")
root.resizable(False, False)
root.bind("<Motion>", move)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
mycar = tkinter.PhotoImage(file="image/car_red.png")
mycar2 = tkinter.PhotoImage(file="image/car_red2.png")
comcar = tkinter.PhotoImage(file="image/car_yellow.png")
set_car()
main()
root.mainloop()
