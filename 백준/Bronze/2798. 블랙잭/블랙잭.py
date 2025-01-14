from itertools import combinations

n,m=map(int,input().split())
card=list(map(int,input().split()))

com=list(combinations(card,3))
sums=[sum(comb) for comb in com]
sums.sort(reverse=True)

for sum in sums:
    if sum<=m:
        result=sum
        break
print(result)

