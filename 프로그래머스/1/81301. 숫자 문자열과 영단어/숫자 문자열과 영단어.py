def solution(s):
    num_list={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = ''
    tmp=''
    
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            tmp+=i
            if tmp in num_list:
                answer+=num_list[tmp]
                tmp=''
    return int(answer)