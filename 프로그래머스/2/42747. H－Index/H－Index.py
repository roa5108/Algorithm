def solution(citations):
    citations.sort()
    arr=[]
    
    for idx, n in enumerate(citations):
        if n>=len(citations)-idx:
            arr.append(len(citations)-idx)
            
    return max(arr) if arr else 0