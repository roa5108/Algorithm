def solution(order):
    answer = 0
    temp = str(order)
    for i in range(len(temp)):
        if temp[i] in ['3','6','9']:
            answer+=1
    return answer