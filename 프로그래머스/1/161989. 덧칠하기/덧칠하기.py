def solution(n, m, section):
    answer = 0
    arr=[1]*n
    for i in section:
        arr[i-1]=0
            
    idx=0
    while idx<n:
        if arr[idx]==0:
            answer+=1
            idx+=m
        else:
            idx+=1
    return answer