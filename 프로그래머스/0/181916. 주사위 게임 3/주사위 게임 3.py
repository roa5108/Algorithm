from collections import Counter
def solution(a, b, c, d):
    counter = Counter([a,b,c,d])
    val = list(counter.values())
    key = list(counter.keys())
    if len(counter) == 1:
        return 1111*a
    if 3 in val:
        p = [k for k,v in counter.items() if v==3][0]
        q = [k for k,v in counter.items() if v==1][0]
        return (10*p+q)**2
    if val.count(2) == 2:
        return (key[0]+key[1]) * abs(key[0]-key[1])
    if 2 in val and 1 in val:
        others = [k for k,v in counter.items() if v==1]
        return others[0] * others[1]
    if len(counter) == 4:
        return min(key)