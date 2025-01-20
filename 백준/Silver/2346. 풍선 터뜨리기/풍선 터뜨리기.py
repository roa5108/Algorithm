import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
balls = list(map(int, input().split()))
deq = deque(range(1, n + 1))

result = []

while deq:
    current_ball = deq.popleft()
    result.append(current_ball)

    move = balls[current_ball - 1]
    if move > 0:
        deq.rotate(-(move - 1))
    else:
        deq.rotate(-move)

print(*result)
