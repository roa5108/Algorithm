def solution(n):
    answer = []
    n=str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))
    return sum(answer)