def solution(babbling):
    answer = 0
    for word in babbling:
        for can in ["aya","ye","woo","ma"]:
            if word.count(can*2)>0:
                continue
            word=word.replace(can," ")
            
        if word.strip()=='':
            answer+=1
    return answer