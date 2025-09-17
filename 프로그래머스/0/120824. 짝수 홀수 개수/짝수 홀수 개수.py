def solution(num_list):
    jcnt, hcnt=0,0
    for i in num_list:
        if i%2==0:
            jcnt+=1
        else:
            hcnt+=1
        
    return [jcnt,hcnt]