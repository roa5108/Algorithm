N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()
for i in range(N):
    print(num[i])
