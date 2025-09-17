import math

def solution(a, b):
    gcd=math.gcd(a,b)
    newB=b//gcd
    while newB%2==0:
        newB=newB//2
    while newB%5==0:
        newB=newB//5
    if newB==5 or newB==1:
            return 1
    else:
        return 2
    