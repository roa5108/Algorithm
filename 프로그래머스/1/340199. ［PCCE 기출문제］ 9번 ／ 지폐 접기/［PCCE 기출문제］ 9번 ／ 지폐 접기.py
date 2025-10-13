def solution(wallet, bill):
    answer = 0
    while (min(wallet[0], wallet[1]) < min(bill[0], bill[1])) or (max(wallet[0], wallet[1]) < max(bill[0], bill[1])):
        if bill[0]>bill[1]:
            bill[0]//=2
        else:
            bill[1]//=2
        answer+=1
    return answer