a=input()
cnt=0
for i in range(len(a)):
    if a[i] == ' ':
        cnt+=1
cnt+=1
if a[0] == ' ':
    cnt-=1
if a[-1]==' ':
    cnt-=1
print(cnt)