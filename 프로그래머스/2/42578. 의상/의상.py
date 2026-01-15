def solution(clothes):
    # 옷 종류별 개수 딕셔너리로 저장
    cnt = {}
    for cloth in clothes:
        cnt[cloth[1]] = cnt.get(cloth[1], 0) + 1
    
    answer = 1
    for c in cnt.values():
        # 옷의 종류 + 1(안입는 경우) 더함
        answer*=(c+1) 
        
    # 아무것도 안입는 경우(모두 선택되지 않은 경우) 제외
    return answer-1