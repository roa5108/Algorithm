def solution(citations):
    citations.sort(reverse=True)
    arr=[]
    print(citations)
    
    for idx, n in enumerate(citations):
        if n>=idx+1:
            arr.append(idx+1)
            
    return max(arr) if arr else 0