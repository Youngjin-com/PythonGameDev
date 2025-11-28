import tkinter
import time
import random

WIDTH, HEIGHT = 960, 720
bg_y = 0
pl_x, pl_y = int(WIDTH/2), HEIGHT-40
cl_x, cl_y = 0, 0
fire = False
SIZE = 80
enemy = []
for i in range(9):
    enemy.append([0,0,0,0,0,0,0,0,0,0,0,0])
scene = "타이틀"
timer = 0
score = 0

def move(e): # 마우스를 움직였을 때
    global pl_x
    if scene=="게임":
        pl_x = int(pl_x*0.9+e.x*0.1)

def click(e): # 클릭했을 때
    global cl_x, cl_y, fire
    cl_x = e.x
    cl_y = e.y
    fire = True

def effect(cx, cy): # 적을 쓰러트리는 연출
    for i in range(10):
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="red")
        cvs.update()
        time.sleep(0.01)
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="yellow")
        cvs.update()
        time.sleep(0.01)

def text(x, y, txt, siz, col): # 그림자효과를 준 문자 표시
    fnt = ("Times New Roman", siz)
    cvs.create_text(x+1, y+1, text=txt, font=fnt, fill="black")
    cvs.create_text(x, y, text=txt, font=fnt, fill=col)

def main(): # 메인 처리를 담당하는 함수
    global bg_y, fire, scene, timer, score
    timer += 1
    bg_y = (bg_y+2)%HEIGHT
    cvs.delete("all")
    cvs.create_image(WIDTH/2, bg_y-HEIGHT/2, image=bg)
    cvs.create_image(WIDTH/2, bg_y+HEIGHT/2, image=bg)
    for y in range(9):
        for x in range(12):
            if enemy[y][x]==1:
                X = x*SIZE + SIZE/2
                Y = y*SIZE + SIZE/2
                cvs.create_image(X, Y, image=invader)
    cvs.create_image(pl_x, pl_y, image=fighter)
    text(WIDTH*0.5, 30, "SCORE "+str(score), 30, "white")

    if scene=="타이틀":
        text(WIDTH*0.5, HEIGHT*0.3, "GALAXY DEFENDER", 60, "cyan")
        if timer%30<15:
            text(WIDTH*0.5, HEIGHT*0.6, "Click to start!", 30, "lime")
        if fire==True:
            for y in range(8):
                for x in range(12):
                    enemy[y][x] = 0
            scene = "게임"
            timer = 0
            score = 0
            fire = False

    if scene=="게임":
        if timer%30==0: # 30프레임마다 1번씩 적을 아래로 이동한다
            for y in range(8, 0, -1):
                for x in range(12):
                    enemy[y][x] = enemy[y-1][x]
            for x in range(12): # 가장 위쪽 행에 새로운 적 출현
                enemy[0][x] = random.choice([0,0,0,1])
            for x in range(12): # 가장 아래쪽 행에 적이 도달했는지 확인
                if enemy[8][x]==1:
                    scene = "게임 오버"
                    timer = 0
        if fire==True: # 화면을 클릭했을 때
           cvs.create_line(pl_x, pl_y, cl_x, cl_y, fill="cyan", width=3)
           fire = False
           ax = int(cl_x/SIZE) # 인덱스(열의 값)를 계산
           ay = int(cl_y/SIZE) # 인덱스(행의 값)를 계산
           if 0<=ax and ax<=11 and 0<=ay and ay<=8: # 적 배열 범위 안에
               if enemy[ay][ax]==1: # 적이 존재하는 경우
                   effect(ax*SIZE, ay*SIZE) # 이펙트를 표시
                   enemy[ay][ax] = 0 # 적을 없앤다
                   score += 100

    if scene=="게임 오버":
        text(WIDTH*0.5, HEIGHT*0.4, "GAME OVER", 60, "red")
        if timer>=30*5:
            scene = "타이틀"
            fire = False

    root.after(33, main)

root = tkinter.Tk()
root.title("갤럭시 디펜더 완성판")
root.resizable(False, False)
root.bind("<Motion>", move)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=WIDTH, height=HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file="image/bg.png")
fighter = tkinter.PhotoImage(file="image/fighter.png")
invader = tkinter.PhotoImage(file="image/invader.png")
main()
root.mainloop()
