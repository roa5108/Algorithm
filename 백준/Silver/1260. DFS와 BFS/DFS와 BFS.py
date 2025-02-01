N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)


def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


def bfs():
    q = [V]
    visited[V] = True
    while q:
        cur = q.pop(0)
        print(cur, end=" ")
        for i in range(1, N + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                q.append(i)


dfs(V)

print()

visited = [False] * (N + 1)
bfs()
