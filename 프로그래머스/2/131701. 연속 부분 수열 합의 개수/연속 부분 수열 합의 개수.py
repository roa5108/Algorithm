def solution(elements):
    arr = elements*2
    lenE = len(elements)
    s = set()
    
    for l in range(1, lenE+1):
        for start in range(lenE):
            s.add(sum(arr[start:start+l]))
    return len(s)