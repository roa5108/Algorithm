def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        new_d=discount[i:i+10]
        for w in range(len(want)):
            if new_d.count(want[w])!=number[w]:
                break
            elif w==len(want)-1:
                answer+=1
    return answer