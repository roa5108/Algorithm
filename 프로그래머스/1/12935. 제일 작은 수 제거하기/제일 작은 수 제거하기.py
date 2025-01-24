def solution(arr):
    s_arr=sorted(arr,reverse=True)
    a=s_arr[-1]
    arr.remove(a)
    return arr if arr else [-1]