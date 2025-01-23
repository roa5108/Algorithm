def solution(s):
    stack=[]
    flag=True
    
    for i in range(len(s)):
        if s[i]=='(':
            stack.append('(')
        else:
            if not stack:
                flag=False
                break
            stack.pop()
            
    if not stack and flag==True:
        return True
    else:
        return False