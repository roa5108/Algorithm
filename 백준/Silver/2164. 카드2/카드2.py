import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
queue = deque(range(1, n + 1))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
