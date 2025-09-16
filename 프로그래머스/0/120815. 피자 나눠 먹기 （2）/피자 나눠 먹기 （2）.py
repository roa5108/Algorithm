def solution(n):
    answer = 0
    if n%6==0:
        return n//6
    else:
        for i in range(1, n+1):
            if 6*i%n==0:
                return i