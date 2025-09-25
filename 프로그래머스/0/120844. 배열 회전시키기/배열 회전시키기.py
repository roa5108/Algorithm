from collections import deque

def solution(numbers, direction):
    d=deque(numbers)
    
    if direction=="right":
        num=d.pop()
        d.appendleft(num)
    else:
        num=d.popleft()
        d.append(num)
    return list(d)