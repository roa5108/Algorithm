def solution(n):
    return fibo(n)%1234567


def fibo(n):
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
        
    return b
        