n = int(input())
coordi = []
for _ in range(n):
    coordi.append(list(map(int, input().split())))

coordi.sort(key=lambda x: (x[1], x[0]))

for x, y in coordi:
    print(x, y)
