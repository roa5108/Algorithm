n = int(input())
num = list(map(int, input().split()))
sorted_num = sorted(set(num))

result = {sorted_num[i]: i for i in range(len(sorted_num))}

for x in num:
    print(result[x], end=" ")
