def solution(n):
    arr=[[0]*n for _ in range(n)]
    dir=[(0,1), (1,0), (0,-1), (-1,0)]
    r, c = 0, 0
    idx=0
    for i in range(1, n**2+1):
        arr[r][c]=i
        
        dr, dc = dir[idx]
        nr, nc = r+dr, c+dc
            
        if nr<0 or nr>=n or nc<0 or nc>=n or arr[nr][nc]!=0:
            idx=(idx+1)%4
            dr, dc = dir[idx]
            nr, nc = r+dr, c+dc
            
        r, c = nr, nc
        
    return arr