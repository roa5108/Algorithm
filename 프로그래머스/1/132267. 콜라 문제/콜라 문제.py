def solution(a, b, n):
    cnt=0
    while n>=a:
        x=(n//a)*b
        n=(n%a)+x
        cnt+=x
    return cnt