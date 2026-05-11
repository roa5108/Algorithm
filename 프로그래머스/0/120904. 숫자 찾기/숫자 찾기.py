def solution(num, k):
    temp=str(num)
    tmp=str(k)
    if tmp in temp:
        return temp.index(tmp)+1
    else: return -1