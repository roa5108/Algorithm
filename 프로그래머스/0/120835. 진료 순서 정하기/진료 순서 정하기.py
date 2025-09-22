def solution(emergency):
    answer=[]
    sorted_e=sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(sorted_e.index(i)+1)
    return answer