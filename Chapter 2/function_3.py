def damage(strength, defense):
    d = strength - defense
    return d

d = damage(100, 20)
print("상대의 공격력이 100, 자신의 방어력이 20일 때 대미지 값은", d)
print("상대의 공격력이 50, 자신의 방어력이 30일 때 대미지 값은", damage(50,30))
