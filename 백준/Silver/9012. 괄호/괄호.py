import sys

input = sys.stdin.readline

n = int(input().strip())


for _ in range(n):
    ps = input().strip()
    stack = []
    is_valid = True

    for i in ps:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                is_valid = False
                break
            stack.pop()

    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
