def solution(dartResult):
    score=""
    result=[]
    rule={"S":1, "D":2, "T":3}
    
    for i in dartResult:
        if i.isdigit():
            score+=i
            
        elif i in rule:
            result.append(int(score)**rule[i])
            score=""
            
        elif i=='#':
            result[-1]*=-1
            
        elif i=='*':
            result[-1]*=2
            if len(result)>=2:
                result[-2]*=2
        
        
    return sum(result)