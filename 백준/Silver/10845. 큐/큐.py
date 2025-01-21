import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        print(-1 if not queue else queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if not queue else 0)
    elif command[0] == "front":
        print(-1 if not queue else queue[0])
    elif command[0] == "back":
        print(-1 if not queue else queue[-1])
