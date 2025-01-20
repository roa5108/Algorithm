n = int(input())
word = []

for _ in range(n):
    word.append(input())


unique_word = list(set(word))  # 중복 제거
unique_word.sort(key=lambda x: (len(x), x))

for i in unique_word:
    print(i)
