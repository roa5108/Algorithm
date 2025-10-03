def solution(a, b):
    answer = 0
    num1=int(str(a)+str(b))
    num2=int(str(b)+str(a))
    return num1 if num1>=num2 else num2