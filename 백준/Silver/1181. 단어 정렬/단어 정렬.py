n = int(input())
word = [input() for _ in range(n)]
w = sorted(set(word), key=lambda x: (len(x), x))

for i in w:
    print(i)
