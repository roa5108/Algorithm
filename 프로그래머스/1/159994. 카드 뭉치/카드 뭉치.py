def solution(cards1, cards2, goal):
    from collections import deque
    answer = ''
    cards1=deque(cards1)
    cards2=deque(cards2)
    tmp=[]
    
    for word in goal:
        if cards1 and cards1[0]==word:
            tmp.append(word)
            cards1.popleft()
            
        elif cards2 and cards2[0]==word:
            tmp.append(word)
            cards2.popleft()
            
        else:
            return 'No'
            
    return 'Yes'