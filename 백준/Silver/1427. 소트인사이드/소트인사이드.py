num = list(map(int, input()))
num.sort(reverse=True)
print("".join(map(str, num)))
