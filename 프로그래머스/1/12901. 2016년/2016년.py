def solution(a, b):
    days=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}
    cnt_day=sum(days[:a-1])
    cnt_day+=b-1
    return week[cnt_day%7]