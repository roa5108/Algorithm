import sys
input=sys.stdin.readline

n=int(input())
num_list=[int(input()) for _ in range(n)]

stack=[]
result=[]
cur=1
for num in num_list:
    while cur<=num:
        stack.append(cur)
        result.append('+')
        cur+=1
        
    if stack[-1]==num:
        stack.pop()
        result.append('-')
        
    else:
        print('NO')
        exit(0)

for op in result:
    print(op)