x_arr = []
y_arr = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x1 = min(x_arr)
x2 = max(x_arr)
y1 = min(y_arr)
y2 = max(y_arr)

print((x2 - x1) * (y2 - y1))