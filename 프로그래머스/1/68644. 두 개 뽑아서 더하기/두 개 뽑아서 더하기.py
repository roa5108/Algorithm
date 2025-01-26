def solution(numbers):
    from itertools import combinations
    answer=[x+y for x,y in list(combinations(numbers,2))]
    return sorted(set(answer))