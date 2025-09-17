def solution(chicken):
    cnt=0
    coupon=chicken
    while coupon>=10:
        newChicken=coupon//10
        cnt+=newChicken
        coupon=coupon%10+newChicken
    return cnt