import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    queue.rotate(-(k - 1))
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
