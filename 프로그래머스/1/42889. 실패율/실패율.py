def solution(N, stages):
    challenger=[0]*(N+2)
    failure={}
    
    for stage in stages:
        challenger[stage]+=1
    
    total=len(stages)
    
    for i in range(1,N+1):
        if challenger[i]==0:
            failure[i]=0
        else:
            failure[i]=challenger[i]/total
            total-=challenger[i]
            
    result=sorted(failure, key=lambda x:failure[x],reverse=True)
    return result