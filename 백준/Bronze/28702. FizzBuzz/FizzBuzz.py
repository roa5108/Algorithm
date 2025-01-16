x=[]
for _ in range(3):
    x.append(input())

for idx,value in enumerate(x):
    if value.isdigit():
        i=int(value)+(3-idx)

if i%15==0:
    print('FizzBuzz') 
elif i%3==0 and i%5!=0:
    print('Fizz') 
elif i%3!=0 and i%5==0:
    print('Buzz') 
else:
    print(i)
