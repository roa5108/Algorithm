import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0] * (N) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    extent = 1
    q = deque([(i, j)])
    graph[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] != 1:
                graph[nx][ny] = 1
                extent += 1
                q.append((nx, ny))
    return extent


extentList = []
cnt = 0
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for a in range(M):
    for b in range(N):
        if graph[a][b] != 1:
            extentList.append(bfs(a, b))
            cnt += 1

print(cnt)
print(" ".join(map(str, sorted(extentList))))
