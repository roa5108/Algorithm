def solution(n):
    n=[int(i) for i in str(n)]
    n.sort(reverse=True)
    n=map(str,n)
    return int(''.join(n))