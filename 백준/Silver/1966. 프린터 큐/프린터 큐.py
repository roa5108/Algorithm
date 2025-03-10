from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    importance=list(map(int,input().split()))
    
    q=deque([(importance[i],i) for i in range(N)])
    cnt=0
    
    while q:
        max_priority=max(q,key=lambda x:x[0])[0]
        priority,index=q.popleft()
        
        if priority==max_priority:
            cnt+=1
            if index==M:
                print(cnt)
                break
            
        else:
            q.append((priority,index))