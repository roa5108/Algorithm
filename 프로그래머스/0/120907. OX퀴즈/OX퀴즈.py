def solution(quiz):
    arr = []
    for i in quiz:
        arr.append(i.split())
    
    result=[]
    print(arr)
    for j in range(len(arr)):
        x, op, y, eq, z = arr[j]
        x, y, z = int(x), int(y), int(z)
        
        if op=='+':
            if x+y==z:
                result.append("O")
            else:
                result.append("X")
        else:
            if x-y==z:
                result.append("O")
            else:
                result.append("X")
    return result