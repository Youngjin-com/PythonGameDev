import tkinter
import time

WIDTH, HEIGHT = 960, 720
bg_y = 0
pl_x, pl_y = 0, HEIGHT-40
cl_x, cl_y = 0, 0
fire = False
SIZE = 80
enemy = [
    [0,0,1,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0,0,0,0,1]
]

def move(e): # 마우스를 움직였을 때
    global pl_x
    pl_x = int(pl_x*0.9+e.x*0.1)

def click(e): # 클릭했을 때
    global cl_x, cl_y, fire
    cl_x = e.x
    cl_y = e.y
    fire = True

def effect(cx, cy): # 적을 쓰러트렸을 때 연출
    for i in range(10):
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="red")
        cvs.update()
        time.sleep(0.01)
        cvs.create_oval(cx, cy, cx+SIZE, cy+SIZE, fill="yellow")
        cvs.update()
        time.sleep(0.01)

def main(): # 메인 처리를 담당하는 함수
    global bg_y, fire
    bg_y = (bg_y+2)%HEIGHT
    cvs.delete("all")
    cvs.create_image(WIDTH/2, bg_y-HEIGHT/2, image=bg)
    cvs.create_image(WIDTH/2, bg_y+HEIGHT/2, image=bg)
    for y in range(3):
        for x in range(12):
            if enemy[y][x]==1:
                X = x*SIZE + SIZE/2
                Y = y*SIZE + SIZE/2
                cvs.create_image(X, Y, image=invader)
    cvs.create_image(pl_x, pl_y, image=fighter)
    if fire==True: # 화면을 클릭했을 때
       cvs.create_line(pl_x, pl_y, cl_x, cl_y, fill="cyan", width=3)
       fire = False
       ax = int(cl_x/SIZE) # 인덱스 (열의 값)를 계산
       ay = int(cl_y/SIZE) # 인덱스 (행의 값)를 계산
       if 0<=ax and ax<=11 and 0<=ay and ay<=2: # 적 배열 범위 안
           if enemy[ay][ax]==1: # 적이 존재할 경우
               effect(ax*SIZE, ay*SIZE) # 이펙트를 표시
               enemy[ay][ax] = 0 # 적을 없앤다
    root.after(33, main)

root = tkinter.Tk()
root.title("갤럭시 디펜더")
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
