n = int(input())
member = [input().split() for _ in range(n)]
member = [(int(age), name) for age, name in member]

member.sort(key=lambda x: x[0])

for age, name in member:
    print(age, name)
