def solution(angle):
    if 0<angle<90:
        return 1
    elif 90<angle<180:
        return 3
    elif angle==180:
        return 4
    else:
        return 2
            