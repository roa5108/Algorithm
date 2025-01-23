def solution(X, Y):
    cnt_X = [0] * 10  # 0부터 9까지 각 숫자의 등장 횟수를 저장할 리스트
    cnt_Y = [0] * 10

    for digit in X:
        cnt_X[int(digit)] += 1
    for digit in Y:
        cnt_Y[int(digit)] += 1

    common_digits = []
    for digit in range(9, -1, -1):  # 9부터 0까지 내림차순으로 확인
        count = min(cnt_X[digit], cnt_Y[digit])
        common_digits.extend([str(digit)] * count)

    if not common_digits:
        return "-1"
    if common_digits[0] == '0':
        return "0"

    return "".join(common_digits)