from collections import deque

def solution(maps):
    answer = 0
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    n=len(maps)
    m=len(maps[0])
    # visited[n][m]=[False*m for _ in range(n)]
    q=deque([(0,0)])
    
    while q:
        curR, curC=q.popleft()
        for i in range(4):
            newR=curR+dr[i]
            newC=curC+dc[i]
            if 0<=newR<n and 0<=newC<m and maps[newR][newC]==1:
                q.append((newR,newC))
                maps[newR][newC]=maps[curR][curC]+1
    return maps[n-1][m-1] if maps[n-1][m-1]>1 else -1