import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

red = 1


def dfs(idx, color):
    visited[idx] = color
    for i in graph[idx]:
        if visited[i] == 0:
            if not dfs(i, -color):
                return False
        elif visited[i] == visited[idx]:
            return False
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_bipartite = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not dfs(i, red):
                is_bipartite = False
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")