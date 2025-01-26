def solution(name, yearning, photo):
    answer = []
    match={name[i]:yearning[i] for i in range(len(name))}
    
    for group in photo:
        score=0
        for person in group:
            if person in match:
                score+=match[person]
        answer.append(score)
    return answer