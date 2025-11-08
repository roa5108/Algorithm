def solution(n):
    one_cnt=str(bin(n)).count('1')
    for i in range(n,1000000):
        if i>n and one_cnt==str(bin(i)).count('1'):
            return i