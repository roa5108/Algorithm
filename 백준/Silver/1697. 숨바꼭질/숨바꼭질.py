from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001


def bfs(v):
    if N == K:
        return 0
    q = deque([(v, 0)])
    visited[v] = True

    while q:
        cur, time = q.popleft()
        for i in [cur - 1, cur + 1, 2 * cur]:
            if i == K:
                return time + 1
            elif 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                q.append((i, time + 1))


print(bfs(N))