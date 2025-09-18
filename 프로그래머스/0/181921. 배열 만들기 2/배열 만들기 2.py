def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(ch in "05" for ch in str(i)):
            answer.append(i)
    return answer if answer else [-1]