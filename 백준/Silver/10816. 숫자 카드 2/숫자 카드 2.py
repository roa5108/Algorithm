import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
compare = list(map(int, input().split()))

count_dict = Counter(card)


def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return count_dict[target]
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


result = [str(binary(card, i, 0, N - 1)) for i in compare]
print(" ".join(result))