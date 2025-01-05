a=input()
b=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
i=0
while i<len(a):
    if a[i:i+3] in b:
        cnt+=1
        i+=3
    elif a[i:i+2] in b:
        cnt+=1
        i+=2
    else:
        cnt+=1
        i+=1

print(cnt)