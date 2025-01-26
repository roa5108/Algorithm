def solution(number):
    from itertools import combinations
    
    arr=list(combinations(number,3))
    cnt=0
    
    for i in arr:
        if sum(i)==0:
            cnt+=1
            
    return cnt