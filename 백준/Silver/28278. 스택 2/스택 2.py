import sys

input = sys.stdin.readline

n = int(input().strip())
stack = []

for i in range(n):
    command = list(map(int, input().strip().split()))

    if command[0] == 1:
        stack.append(command[1])

    elif command[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 3:
        print(len(stack))

    elif command[0] == 4:
        print(1 if not stack else 0)

    elif command[0] == 5:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
