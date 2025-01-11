word=[list(input()) for _ in range(5)]
result=''

for i in range(max(len(row) for row in word)): #가장 긴 행 길이
    for j in range(5):
        if i<len(word[j]): #해당 열이 현재 행에 존재하는지 확인
            result+=word[j][i]
print(result)