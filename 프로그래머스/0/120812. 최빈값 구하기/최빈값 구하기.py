from collections import Counter

def solution(array):
    counter=Counter(array)
    most=counter.most_common()
    if len(most)>1 and most[0][1]==most[1][1]:
        return -1
    else:
        return most[0][0]