def solution(participant, completion):
    dic={}
    for p in participant:
        dic[p]=dic.get(p,0)+1
    
    for c in completion:
        dic[c]-=1
        
    for name, cnt in dic.items():
        if cnt>0:
            return name