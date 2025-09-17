def solution(my_string, n):
    answer = ''
    arr=list(my_string)
    print(arr)
    for i in arr:
        answer+=i*n
    return answer