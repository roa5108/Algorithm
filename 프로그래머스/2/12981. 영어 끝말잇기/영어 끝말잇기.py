def solution(n, words):
    answer=[0,0]
    arr=[]
    for i in range(len(words)):
        if arr:
            if words[i] in arr or words[i][0]!=arr[-1][-1]:
                return [i%n+1,i//n+1]
        arr.append(words[i])
    return answer