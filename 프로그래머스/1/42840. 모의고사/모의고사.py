def solution(answers):
    answer=[]
    score = [0,0,0]
    n1=[1,2,3,4,5]
    n2=[2,1,2,3,2,4,2,5]
    n3=[3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i]==n1[i%len(n1)]:
            score[0]+=1
        if answers[i]==n2[i%len(n2)]:
            score[1]+=1
        if answers[i]==n3[i%len(n3)]:
            score[2]+=1
    
    for idx,n in enumerate(score):
        if n==max(score):
            answer.append(idx+1)
    
    return answer