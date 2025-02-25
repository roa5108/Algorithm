x_count = {}
y_count = {}

for _ in range(3):
    x, y = map(int, input().split())

    # x 좌표 개수 세기
    x_count[x] = x_count.get(x, 0) + 1

    # y 좌표 개수 세기
    y_count[y] = y_count.get(y, 0) + 1

# 한 번만 등장한 x, y 좌표 찾기
for key in x_count:
    if x_count[key] == 1:
        fourth_x = key

for key in y_count:
    if y_count[key] == 1:
        fourth_y = key

print(fourth_x, fourth_y)
