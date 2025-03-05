import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R=map(int,input().split())

visited=[False]*(N+1)
graph={i:[] for i in range(1,N+1)}
ans=[0]*(N+1)


for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()
    
order=1

def dfs(idx):
    global order
    visited[idx]=True
    ans[idx]=order
    for i in graph[idx]:
        if not visited[i]:
            order+=1
            dfs(i)
            
dfs(R)
print('\n'.join(map(str,ans[1:])))