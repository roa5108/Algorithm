from math import factorial

def solution(n):
    m=0
    index=0
    for i in range(1,11):
        if factorial(i)>m and factorial(i)<=n:
            m=factorial(i)
            index=i
            
    return index