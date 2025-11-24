def solution(k, tangerine):
    d={}
    for i in tangerine:
        d[i]=d.get(i,0)+1
    
    sorted_d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    result=0
    cnt=0
    
    for size, num in sorted_d:
        result+=num
        cnt+=1
        if result>=k:
            return cnt