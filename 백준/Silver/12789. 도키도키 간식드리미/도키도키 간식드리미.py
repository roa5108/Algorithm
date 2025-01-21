import sys

input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
stack = []
line = []
current = 1

for person in people:
    while stack and stack[-1] == current:
        line.append(stack.pop())
        current += 1

    if person == current:
        line.append(person)
        current += 1
    else:
        stack.append(person)

while stack and stack[-1] == current:
    line.append(stack.pop())
    current += 1

if line == sorted(people):
    print("Nice")
else:
    print("Sad")
