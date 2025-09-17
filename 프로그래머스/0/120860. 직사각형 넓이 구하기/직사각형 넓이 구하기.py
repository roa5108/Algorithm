def solution(dots):
    arr=sorted(dots,key=lambda x:x[0])
    print(arr)
    answer=abs((arr[1][1]-arr[0][1])*(arr[2][0]-arr[0][0]))
    return answer