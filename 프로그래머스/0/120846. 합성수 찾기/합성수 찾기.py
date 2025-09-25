def solution(n):
    cnt2=0
    for i in range(1,n+1):
        cnt1=0
        for j in range(1,n+1):
            if i%j==0:
                cnt1+=1
        if cnt1>=3:
            cnt2+=1
    return cnt2