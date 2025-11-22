n=int(input())
for i in range(1,n+1):
    s=str(i)
    cnt=sum(1 for ch in s if ch in '369')

    if cnt>0:
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ")