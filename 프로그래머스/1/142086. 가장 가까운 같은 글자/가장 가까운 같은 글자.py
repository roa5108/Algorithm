def solution(s):
    arr = ''
    result=[]
    for i in range(len(s)):
        if s[i] not in arr:
            arr+=s[i]
            result.append(-1)
        else:
            result.append(i-arr.rfind(s[i]))
            arr+=s[i]
    return result