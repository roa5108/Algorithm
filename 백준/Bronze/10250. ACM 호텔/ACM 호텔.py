import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    h,w,n=map(int,input().split())
    if n%h==0:
        floor=h
    else:
        floor=n%h
    num=(n-1)//h+1
    room=floor*100+num
    print(room)