from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열에서 값이 1인 위치(익은 토마토)를 모두 찾기
def find_ones(graph):
    ones=[(i,j) for i in range(N) for j in range(M) if graph[i][j]==1]
    return ones

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph):
    # 초기 익은 토마토(1)의 위치를 큐에 삽입
    q=deque(find_ones(graph))
    days=-1 # 첫날을 0일로 두고, 탐색이 진행될 때마다 +1
    while q:
        for _ in range(len(q)): # 현재 큐에 있는 모든 요소를 동시에 처리
            x,y=q.popleft()
            for k in range(4):
                nx,ny=x+dx[k],y+dy[k]
                if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1 # 익히는 날짜 저장
                    q.append((nx,ny))
        days+=1 # 하루 경과
        
    # 익지 않은 토마토(0)가 남아 있다면 -1 반환    
    return days if all(0 not in row for row in graph) else -1

print(bfs(tomatoes))