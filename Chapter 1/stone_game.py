import random
import time
print("""
돌 줍기 게임의 규칙：
돌의 개수는 랜덤으로 정해집니다.(15 ~ 22개)
선공,후공도 랜덤으로 정해집니다.
플레이어와 컴퓨터가 각자 1 ~ 3개를 줍습니다.
마지막 1개를 주운 쪽이 패배합니다.
남은 개수가 3개이하일 때 전부 주우면 패배합니다.
""")

stone = random.randint(15, 22)
turn = random.randint(0, 1)
take = 0

while stone>0:
    turn = 1 - turn
    print("-"*40)
    for i in range(stone):
        print("●", end="")
    print(" 돌의 개수", stone)
    if turn==0:
        print("당신 차례입니다")
        while True:
            i = input("몇개를 주우시겠습니까?")
            if i=="1" and stone>0:
                take = 1
                break
            if i=="2" and stone>1:
                take = 2
                break
            if i=="3" and stone>2:
                take = 3
                break
        print("당신은", take, "개를 주웠습니다.")
    else:
        print("컴퓨터의 차례입니다.")
        take = (stone-1)%4
        if take==0:
            take = random.randint(1,3)
            if take>stone: take = stone
        time.sleep(2)
        print(take, "개를 주웠습니다.")
    stone = stone - take
    time.sleep(2)

print("-------------- 게임 종료 --------------")
if turn==1:
    print("당신의 승리입니다!")
else:
    print("컴퓨터의 승리입니다!")
