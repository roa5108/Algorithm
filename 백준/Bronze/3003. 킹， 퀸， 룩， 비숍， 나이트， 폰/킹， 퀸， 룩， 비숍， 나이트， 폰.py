a=[1,1,2,2,2,8]
b=list(map(int,input().split()))
c=[]
for i in range(6):
    c.append(a[i]-b[i])
print(" ".join(map(str,c)))