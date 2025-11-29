def solution(prices):
    answer = []
    for i in range(len(prices)):
        flag=0
        for j in range(i+1, len(prices)):
            flag+=1
            if prices[i]>prices[j]:
                break
        answer.append(flag)
    return answer