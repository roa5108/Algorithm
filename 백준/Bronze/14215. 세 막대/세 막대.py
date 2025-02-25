slides = list(map(int, input().split()))
a, b, c = sorted(slides)
if a + b <= c:
    c = a + b - 1
print(a + b + c)