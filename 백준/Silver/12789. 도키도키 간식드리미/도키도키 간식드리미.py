import sys

input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
stack = []
current = 1

for person in people:
    stack.append(person)

    while stack and stack[-1] == current:
        stack.pop()
        current += 1

if not stack:
    print("Nice")
else:
    print("Sad")