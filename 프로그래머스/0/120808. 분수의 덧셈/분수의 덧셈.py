import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    top=numer1*denom2+numer2*denom1
    bottom=denom1*denom2
    g=math.gcd(top,bottom)
    answer.extend([top/g, bottom/g])
    return answer