def solution(nums):
    answer = 0

    from itertools import combinations
    comb=list(combinations(nums,3))
    sum_comb=[sum(x) for x in comb]
    
    def is_Prime(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    return sum(1 for i in sum_comb if is_Prime(i))