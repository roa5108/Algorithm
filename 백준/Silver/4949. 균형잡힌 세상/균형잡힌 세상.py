import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break

    stack = []
    flag = True

    for i in sentence:
        if i == "(" or i == "[":
            stack.append(i)

        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break

        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack:
        print("yes")
    else:
        print("no")
