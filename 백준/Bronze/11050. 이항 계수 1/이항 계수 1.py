import sys
import math
input=sys.stdin.readline

n,k=map(int,input().split())
binomial=math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
print(binomial)