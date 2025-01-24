def solution(s):
    words = s.split(' ')  # 단어를 공백 기준으로 나누되, 공백을 포함해 유지
    result = []
    
    for word in words:
        new_word = ''
        for j in range(len(word)):
            if j % 2 == 0:  # 짝수 인덱스
                new_word += word[j].upper()
            else:  # 홀수 인덱스
                new_word += word[j].lower()
        result.append(new_word)
    
    return ' '.join(result)  # 단어를 공백으로 다시 연결
