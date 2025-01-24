def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1]==i:
            answer.pop()
        answer.append(i)
        
    return answer