a_attack, a_life = map(int, input().split())
b_attack, b_life = map(int, input().split())

while True:
    a_life -= b_attack
    b_life -= a_attack
    
    if a_life <= 0 and b_life <= 0:
        print("DRAW")
        break

    elif a_life <= 0:
        print("PLAYER B")
        break
    
    elif b_life <= 0:
        print("PLAYER A")
        break
