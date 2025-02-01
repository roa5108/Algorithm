n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
            cnt += dfs(nx, ny)

    return cnt

cntList = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            cntList.append(dfs(i, j))

print(len(cntList))
cntList.sort()
for i in cntList:
    print(i)