import sys

input = sys.stdin.readline

n = int(input())
num = set(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))

for i in compare:
    if i in num:
        print(1)
    else:
        print(0)
