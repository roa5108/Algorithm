n = int(input())
yaksu = list(map(int, input().split()))
yaksu.sort()
print(yaksu[0] * yaksu[-1])