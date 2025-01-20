import sys

input = sys.stdin.readline
n = input().strip()
num = []

for i in range(len(n)):
    num.append(int(n[i]))
    
num.sort(reverse=True)
print("".join(map(str, num)))
