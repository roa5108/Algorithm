def solution(num, total):
    result=[0]*num
    mid=0
    
    if num%2!=0:
        mid=num//2
        result[mid]=total//num
    else:
        mid=num//2-1
        result[mid]=total//num
            
    for i in range(mid+1,num):
        result[i]=result[i-1]+1
    for j in range(mid-1, -1, -1):
        result[j]=result[j+1]-1
        
    return result
    