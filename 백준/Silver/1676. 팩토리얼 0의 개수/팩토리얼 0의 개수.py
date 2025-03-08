N = int(input())


def factorial(val):
    if val == 1 or val == 0:
        return 1
    else:
        return val * factorial(val - 1)


fact = str(factorial(N))
zero_cnt = 0

for i in fact[::-1]:
    if i == "0":
        zero_cnt += 1
    else:
        break

print(zero_cnt)