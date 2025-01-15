from collections import Counter
a=int(input())
b=int(input())
c=int(input())
product=str(a*b*c)
counter=Counter(product)

for digit in range(10):
    print(counter[str(digit)])