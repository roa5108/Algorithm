def solution(price, money, count):
    cost=0
    for i in range(1,count+1):
        cost+=i*price
    return cost-money if cost>money else 0