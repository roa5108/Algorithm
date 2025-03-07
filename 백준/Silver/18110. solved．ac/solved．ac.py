import sys
input=sys.stdin.readline

n=int(input())
op=[]

for _ in range(n):
    op.append(int(input()))
    
op.sort()

def my_round(val):
    if val - int(val)>=0.5:
        return int(val)+1
    else:
        return int(val)    

minus=my_round(n*0.15)

def level(arr):
    if n==0:
        return 0
    new_arr=arr[minus:n-minus]
    return my_round(sum(new_arr)/len(new_arr))

print(level(op))