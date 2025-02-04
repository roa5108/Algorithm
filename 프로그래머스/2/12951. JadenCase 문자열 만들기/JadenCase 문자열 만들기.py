def solution(s):
    arr = s.split(" ")
    new_arr = []
    
    for word in arr:
        if len(word)>0 and word[0].isalpha():  # 첫 글자가 알파벳이면
            new_word = word[0].upper() + word[1:].lower()  # 첫 글자는 대문자, 나머지는 소문자
        else:
            new_word = word.lower()  # 숫자로 시작하면 전체를 소문자로 변환
        
        new_arr.append(new_word)
    
    return " ".join(new_arr)