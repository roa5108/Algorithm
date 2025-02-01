n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

cnt = 0

def bfs():
    global cnt
    q = [1]
    visited[1] = True
    while q:
        cur = q.pop(0)
        cnt += 1
        for i in range(1, n + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                q.append(i)

bfs()
print(cnt - 1)