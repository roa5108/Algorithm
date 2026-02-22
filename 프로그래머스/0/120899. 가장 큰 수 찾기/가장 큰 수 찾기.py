def solution(array):
    m = max(array)
    return [max(array), array.index(m)]