def solution(ingredient):
    answer = 0
    hamburger=[1,2,3,1]
    stack=[]
    for i in ingredient:
        stack.append(i)
        if len(stack)<4:
            continue
        if stack[-4:]==hamburger:
            for i in range(4):
                stack.pop()
            answer+=1
    return answer