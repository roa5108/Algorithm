def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list)-1,n):
        arr=[]
        for j in range(n):
            arr.append(num_list[i+j])
        
        answer.append(arr)
    return answer