def solution(s):
    arr_s=list(map(int,s.split()))
    result=[min(arr_s),max(arr_s)]
    return ' '.join(map(str,result))