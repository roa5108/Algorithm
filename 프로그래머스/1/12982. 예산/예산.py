def solution(d, budget):
    answer = 0
    d.sort()
    sum=0
    for i in d:
        sum+=i
        if sum<=budget:
            answer+=1
    return answer