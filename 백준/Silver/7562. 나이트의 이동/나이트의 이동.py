from collections import deque
import sys
input=sys.stdin.readline

#시계방향으로(오른쪽 위부터)
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]


def bfs(i,j,gA,gB,N):
    if (i,j)==(gA,gB):
        print(0)
        return
    
    q=deque([(i,j)])
    graph=[[-1]*N for _ in range(N)]
    graph[i][j]=0
    
    while q:
        x,y=q.popleft()
        for k in range(8):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==-1:
                graph[nx][ny]=graph[x][y]+1
                if nx==gA and ny==gB:
                    print(graph[gA][gB])
                    return
                q.append((nx,ny))
             
             
T=int(input())
for _ in range(T):
    N=int(input())
    a,b=map(int,input().split())
    gA,gB=map(int,input().split())
    bfs(a,b,gA,gB,N)