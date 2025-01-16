import sys
input=sys.stdin.readline

while True:
    length=list(map(int,input().split()))
    if length==[0,0,0]:
        break
    length.sort()
    a,b,c=length
    
    if a**2+b**2==c**2:
        print('right')
    else:
        print('wrong')