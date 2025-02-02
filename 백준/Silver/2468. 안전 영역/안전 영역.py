import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, k):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and graph[nx][ny] > k
            ):
                visited[nx][ny] = True
                q.append((nx, ny))


cntList = []
for k in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for a in range(N):
        for b in range(N):
            if not visited[a][b] and graph[a][b] > k:
                bfs(a, b, k)
                cnt += 1
    cntList.append(cnt)

print(max(cntList))
