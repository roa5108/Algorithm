def solution(k, m, score):
    score.sort(reverse=True)
    box=[]
    result=0
    
    for i in range(0,len(score),m):
        box.append([x for x in score[i:i+m]])
    
    for j in range(len(box)):
        if len(box[j])==m:
            result+=min(box[j])*m

    return result