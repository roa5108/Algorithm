def solution(k, score):
    arr = []
    answer=[]
    for i in range(len(score)):
        arr.append(score[i])
        arr.sort(reverse=True)
        if len(arr)>k:
            arr.pop()
        answer.append(arr[-1])
    return answer