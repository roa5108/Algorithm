import sys
input=sys.stdin.readline

n=int(input())
t_num=list(map(int,input().split()))
t,p=map(int,input().split())

cnt=0
for i in t_num:
    if i==0:
        continue
    if i<=t:
        cnt+=1
    else:
        if i%t==0:
            cnt+=i//t
        else:
            cnt+=(i//t)+1
print(cnt)
print(n//p,n%p)