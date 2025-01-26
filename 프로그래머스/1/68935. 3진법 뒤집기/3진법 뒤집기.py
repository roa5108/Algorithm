def solution(n):
    result=[]
    while n>0:
        result.append(n%3)
        n=n//3
        
    ans=0
    for i in range(len(result)):
        ans+=result.pop()*3**i
    
    return ans