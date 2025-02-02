import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = {}


def dfs(idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            parent[i] = idx
            dfs(i)


dfs(1)
for i in range(2, N + 1):
    print(parent[i])