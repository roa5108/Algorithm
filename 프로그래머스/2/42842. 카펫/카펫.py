def solution(brown, yellow):
    answer = []
    r,c = 0,0
    rc=brown+yellow
    for i in range(2, rc-1):
        if rc%i==0:
            r=i
            c=rc//i
            if (r+c-2)*2==brown:
                return [r,c] if r>c else [c,r]