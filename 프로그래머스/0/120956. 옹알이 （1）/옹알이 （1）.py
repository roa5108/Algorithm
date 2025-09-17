def solution(babbling):
    result=0
    arr = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for i in range(4): # arr 길이만큼 반복해 모든 단어 startwith 검사
            for word in arr:
                if word in b and b.startswith(word): # wyeoo에서 ye 삭제 시 woo가 남아 정상 단어 처리되는 경우 제외
                    b = b.replace(word, "")
        if b=="": # 모두 삭제되면 가능한 단어이므로 result+1
            result+=1
            
    return result