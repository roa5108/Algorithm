n = int(input())
coordi = []
for _ in range(n):
    coordi.append(list(map(int, input().split())))

coordi.sort(key=lambda x: (x[0], x[1]))

for x, y in coordi:
    print(x, y)
