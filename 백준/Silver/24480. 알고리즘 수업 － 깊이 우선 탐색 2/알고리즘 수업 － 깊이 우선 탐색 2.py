import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in range(1, N + 1):
    graph[key].sort(reverse=True)


cnt = 1


def dfs(idx):
    global cnt
    visited[idx] = cnt
    for i in graph[idx]:
        if not visited[i]:
            cnt += 1
            dfs(i)


dfs(R)
print("\n".join(map(str, visited[1:])))