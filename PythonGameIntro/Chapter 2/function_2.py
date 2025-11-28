def life_check(val):
    if val>0:
        print("아직 싸울 수 있습니다.")
    else:
        print("더 이상 싸울 수 없습니다.")

print("체력 값 100에서 함수를 실행")
life_check(100)
print("체력 값 0에서 함수를 실행")
life_check(0)
