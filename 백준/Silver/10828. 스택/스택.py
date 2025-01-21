import sys

input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        print(-1 if not stack else stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if not stack else 0)
    elif command[0] == "top":
        print(-1 if not stack else stack[-1])
