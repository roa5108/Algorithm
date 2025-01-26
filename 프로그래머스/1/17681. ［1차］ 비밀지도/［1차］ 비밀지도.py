def solution(n, arr1, arr2):
    answer=[]
    bin_arr1 = [format(i, f'0{n}b') for i in arr1]
    bin_arr2 = [format(j, f'0{n}b') for j in arr2]
    
    for i in range(n):
        row=''
        for j in range(n):
            if bin_arr1[i][j]=='1' or bin_arr2[i][j]=='1':
                row+='#'
            else:
                row+=' '
        answer.append(row)
    return answer