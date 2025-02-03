from collections import deque

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]
diff = [-1, 1]


def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        if graph[x][y] == "-":
            for i in range(2):
                ny = y + diff[i]
                if 0 <= ny < M and not visited[x][ny] and graph[x][ny] == "-":
                    visited[x][ny] = True
                    q.append((x, ny))
        elif graph[x][y] == "|":
            for i in range(2):
                nx = x + diff[i]
                if 0 <= nx < N and not visited[nx][y] and graph[nx][y] == "|":
                    visited[nx][y] = True
                    q.append((nx, y))


cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)
