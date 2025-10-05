def solution(num_list):
    hol, jjak='',''
    for i in num_list:
        if i%2==0:
            jjak+=str(i)
        else:
            hol+=str(i)
    return int(jjak)+int(hol)