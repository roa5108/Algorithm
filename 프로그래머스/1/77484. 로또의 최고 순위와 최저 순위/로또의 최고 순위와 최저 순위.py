def solution(lottos, win_nums):
    cnt=0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt+=1
            
    if cnt+lottos.count(0)>1:
        max_rank=7-(cnt+lottos.count(0))
    else:
        max_rank=6
        
    if cnt>1:
        min_rank=7-cnt
    else:
        min_rank=6
        
    rank=[max_rank,min_rank]
    
    return rank