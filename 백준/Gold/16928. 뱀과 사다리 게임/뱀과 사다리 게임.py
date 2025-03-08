import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

ladder = {}
snake = {}
visited = [0] * 101

for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(M):
    c, d = map(int, input().split())
    snake[c] = d


def bfs(idx):
    visited[idx] = 1
    q = deque([idx])
    while q:
        now = q.popleft()
        for dice in range(1, 7):
            next = now + dice
            if next == 100:
                return visited[now]
            if next in ladder:
                next = ladder[next]
            if next in snake:
                next = snake[next]
            if next <= 100 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


print(bfs(1))
