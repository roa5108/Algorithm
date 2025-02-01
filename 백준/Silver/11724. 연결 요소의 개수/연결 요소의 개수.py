import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(idx):
    visited[idx] = True
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


cnt = 0
for k in range(1, N + 1):
    if visited[k] == False:
        dfs(k)
        cnt += 1

print(cnt)
