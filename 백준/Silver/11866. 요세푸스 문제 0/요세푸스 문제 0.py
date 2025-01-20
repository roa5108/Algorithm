import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
