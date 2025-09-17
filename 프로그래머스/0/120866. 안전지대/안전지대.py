dr=[-1,1,0,0,-1,-1,1,1]
dc=[0,0,-1,1,-1,1,-1,1]

def solution(board):
    row=len(board)
    col=len(board[0])
    
    for i in range(row):
        for j in range(col):
            if board[i][j]==1:
                for k in range(8):
                    nr=i+dr[k]
                    nc=j+dc[k]
                    if 0<=nr<row and 0<=nc<col and board[nr][nc]==0:
                        board[nr][nc]=-1
    cnt=0
    for i in range(row):
        for j in range(col):
            if board[i][j]==0:
                cnt+=1
    return cnt