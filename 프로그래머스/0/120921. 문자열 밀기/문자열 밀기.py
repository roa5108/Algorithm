from collections import deque

def solution(A, B):
    listA=list(A)
    listB=list(B)
    q=deque(listA)
    
    cnt=0
    for i in range(len(A)):
        if list(q)!=listB:
            s=q.pop()
            q.appendleft(s)
            cnt+=1
        else:
            return cnt
    return -1