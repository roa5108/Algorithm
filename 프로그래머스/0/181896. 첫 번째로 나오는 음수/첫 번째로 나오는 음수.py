def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:
            return i
        if i==len(num_list)-1:
            return -1