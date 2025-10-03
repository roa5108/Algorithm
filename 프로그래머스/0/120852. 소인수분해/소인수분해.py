import math

def solution(n):
    answer = []
    for i in range(2, int(math.sqrt(n))+1):
        while n%i==0:
            if i not in answer:
                answer.append(i)
            n//=i
    if n>1:
        answer.append(n)
    return answer