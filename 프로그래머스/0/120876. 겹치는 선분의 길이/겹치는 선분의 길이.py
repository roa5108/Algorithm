def solution(lines):
    cover=[0]*201 #-100~100 cover
    
    for a, b in lines:
        a, b = min(a,b), max(a,b)
        for x in range(a,b):
            cover[x+100]+=1
        
    return sum(1 for c in cover if c>=2)