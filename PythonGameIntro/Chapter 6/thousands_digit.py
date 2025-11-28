print("좋아하는 정수를 입력해주세요")
print("입력하지 않고 Enter를 누르면 종료됩니다")
while True:
    s = input("입력할 값은 ")
    if s=="": break
    n = int(s)
    i = int(n/1000)
    t = i%10
    print("이 값의 천 자리의 숫자는 ", t, "입니다")
