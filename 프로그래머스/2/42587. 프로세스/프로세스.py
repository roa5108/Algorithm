from collections import deque

def solution(priorities, location):
    order = 0
    dq = deque([(idx, key) for idx, key in enumerate(priorities)])
    
    while dq:
        cur = dq.popleft()
        if any(cur[1]<x[1] for x in dq):
            dq.append(cur)
        else:
            order+=1
            if cur[0]==location:
                return order
