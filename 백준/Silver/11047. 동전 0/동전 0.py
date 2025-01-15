n,k=map(int,input().split())
a=[]
for _ in range(n):
    num=int(input())
    if k//num!=0:
        a.append(num)
a.sort(reverse=True)

result=0
for i in range(len(a)):
    result+=(k//a[i])
    k%=a[i]
print(result)