import sys
input=sys.stdin.readline

n=int(input())
distance=list(map(int,input().split()))
cost=list(map(int,input().split()))

result=0
min_cost=cost[0]

for i in range(n-1):
    if cost[i]<min_cost:
        min_cost=cost[i]
    result+=min_cost*distance[i]
print(result)