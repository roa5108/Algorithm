import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(idx, goal, cnt):
    if idx == goal:
        return cnt

    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            result = dfs(i, goal, cnt + 1)
            if result != -1:
                return result

    return -1


print(dfs(person1, person2, 0))