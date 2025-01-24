def solution(t, p):
    arr= [t[i:i+len(p)] for i in range(len(t)-len(p)+1)]
    cnt=0
    for x in arr:
        if x<=p:
            cnt+=1
    return cnt