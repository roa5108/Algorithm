from collections import deque
import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort(reverse=True)

def bfs(idx):
    queue=deque([idx])
    visited[idx]=1
    
    cnt=2
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0: 
                visited[i]=cnt
                cnt+=1
                queue.append(i)
                

bfs(R)
for i in range(1,N+1):
    print(visited[i])