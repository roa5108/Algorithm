a, b = map(int, input().split())
c=a*60+b
result=(c-45)//60
result2=(c-45)%60
if(result<0):
    print(result+24,result2)
else:
    print(result,result2)
