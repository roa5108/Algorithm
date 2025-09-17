def solution(dots):
    
    # 외적 비교로 평행 체크 (정수 연산)
    def is_par(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
           
        return  (y2 - y1)*(x4 - x3) == (y4 - y3)*(x2 - x1)
        
    a,b,c,d = dots
    
    if is_par(a,b,c,d): return 1
    if is_par(a,c,b,d): return 1
    if is_par(a,d,b,c): return 1

    return 0