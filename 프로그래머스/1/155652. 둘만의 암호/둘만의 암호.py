def solution(s, skip, index):
    answer = ''
    for i in s:
        temp=i
        move=0
        
        while move<index:
            temp=chr(ord(temp)+1)
            if temp>'z':
                temp='a'
            if temp in skip:
                continue
            move+=1
        answer+=temp
        
    return answer