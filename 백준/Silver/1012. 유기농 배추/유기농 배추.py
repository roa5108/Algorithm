import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if visited[x][y] or graph[x][y] == 0:
        return

    visited[x][y] = True

    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        dfs(cx, cy)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
