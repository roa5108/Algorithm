def solution(num_list):
    hol = sum(list(num_list[a] for a in range(len(num_list)) if a%2!=0))
    jjak = sum(list(num_list[a] for a in range(len(num_list)) if a%2==0))
    return max(hol,jjak)