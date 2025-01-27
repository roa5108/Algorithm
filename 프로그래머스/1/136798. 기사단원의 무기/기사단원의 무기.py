def solution(number, limit, power):
    yaksu=[]
    for i in range(1,number+1):
        cnt=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                cnt+=1
                if i//j!=j:
                    cnt+=1
        yaksu.append(cnt)
        
    for k in range(len(yaksu)):
        if yaksu[k]>limit:
            yaksu[k]=power
    return sum(yaksu)