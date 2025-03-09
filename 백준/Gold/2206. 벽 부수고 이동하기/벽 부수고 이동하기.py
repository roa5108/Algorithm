import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방문 배열: [벽을 안 부쉈을 때, 벽을 부쉈을 때]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, broken = q.popleft()

        # 목표 지점에 도달했으면 그때의 방문 값을 반환
        if x == N - 1 and y == M - 1:
            return visited[broken][x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 부수지 않았을 때 벽을 만났을 경우
                if graph[nx][ny] == 1 and broken == 0 and visited[1][nx][ny] == 0:
                    visited[1][nx][ny] = visited[broken][x][y] + 1
                    q.append((nx, ny, 1))

                # 벽을 부수지 않고 빈 공간을 지나갈 경우
                if graph[nx][ny] == 0 and visited[broken][nx][ny] == 0:
                    visited[broken][nx][ny] = visited[broken][x][y] + 1
                    q.append((nx, ny, broken))

    return -1 #목적지에 도달할 수 없으면 -1을 반환


print(bfs())