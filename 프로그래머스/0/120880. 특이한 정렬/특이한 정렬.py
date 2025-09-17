def solution(numlist, n):
    arr={num: abs(num-n) for _, num in enumerate(numlist)}
    s_arr=dict(sorted(arr.items(), key=lambda x:(x[1], -x[0])))
    answer=list(s_arr.keys())
    return answer