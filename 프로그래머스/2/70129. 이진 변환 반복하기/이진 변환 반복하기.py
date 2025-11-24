def solution(s):
    cnt1,cnt2=0,0
    while s!='1':
        for i in s:
            if i=='0':
                s=s.replace('0','')
                cnt1+=1
        c=len(s)
        s=bin(c)[2:]
        cnt2+=1
    return [cnt2,cnt1]