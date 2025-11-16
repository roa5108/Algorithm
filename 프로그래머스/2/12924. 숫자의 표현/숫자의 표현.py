def solution(n):
    answer=0
    prefix_sum=[0]
    for i in range(1, n+1):
        prefix_sum.append(prefix_sum[-1]+i)
        
    left, right = 0, 1
    while right<len(prefix_sum):
        current=prefix_sum[right]-prefix_sum[left]
        if current==n:
            answer+=1
            left+=1
        elif current<n:
            right+=1
        else:
            left+=1
    return answer