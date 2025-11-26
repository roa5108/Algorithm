from math import comb

def solution(n):
    answer = 0
    max_two=n//2    #최대가 되는 2의 개수
    for two in range(max_two+1):
        one=n-2*two    #one은 1의 개수, two는 2의 개수
        answer+=comb(one+two, two)  #1과 2의 개수를 구하고 전체에서 2가 들어갈 자리를 고르는 조합
    return answer%1234567