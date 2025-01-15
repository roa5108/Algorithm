n=int(input())
for _ in range(n):
    OX=input()
    score=0
    current_score=0

    for i in range(len(OX)):
        if OX[i]=='O':
            current_score+=1
            score+=current_score
        else:
            current_score=0
    print(score)