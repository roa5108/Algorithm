def solution(participant, completion):
    player={}
    
    for i in participant:
        if i in player:
            player[i]+=1
        else:
            player[i]=1
            
    for j in completion:
        player[j]-=1
        
    for j in player:
        if player[j]>0:
            return j