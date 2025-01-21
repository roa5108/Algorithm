def hannoi(n, current, target, assistant):
    if n == 0:
        return
    hannoi(n - 1, current, assistant, target)
    print(current, target)
    hannoi(n - 1, assistant, target, current)


n = int(input())
print(2**n - 1)
hannoi(n, 1, 3, 2)
