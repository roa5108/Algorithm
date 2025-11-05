def solution(keymap, targets):
    answer = []
    MAX=100000
    for i in range(len(targets)):
        count=0
        for j in targets[i]:
            idx=MAX
            for k in range(len(keymap)):
                if j in keymap[k]:
                    idx=min(idx,keymap[k].index(j)+1)
            count+=idx
        answer.append(count) if count<MAX else answer.append(-1)
    return answer