def solution(n, lost, reserve):
    ans=0
    lost.sort()
    reserve.sort()
    
    for i in range(1,n+1):
        if i not in lost:
            ans+=1
            
    for i in lost:
        if i in reserve:
            ans+=1
            reserve.remove(i)
            
        elif i-1 in reserve and i-1 not in lost:
            ans+=1
            reserve.remove(i-1)
            
        elif i+1 in reserve and i+1 not in lost:
            ans+=1
            reserve.remove(i+1)
            
    return ans