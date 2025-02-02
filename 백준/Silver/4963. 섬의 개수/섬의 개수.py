import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상하좌우, 좌상,우상,좌하,우하 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)