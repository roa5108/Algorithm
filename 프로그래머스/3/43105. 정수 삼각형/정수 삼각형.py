def solution(triangle):
    n=len(triangle)
    dp=[[0]*len(row) for row in triangle]
            
    dp[0][0]=triangle[0][0]
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            # 왼쪽 위에서 오른쪽 아래 대각선
            if j>0:
                left=dp[i-1][j-1]
            else:
                left=0
                
            # 오른쪽 위에서 왼쪽 아래 대각선
            if j<len(triangle[i-1]):
                right=dp[i-1][j]
            else:
                right=0
            
            dp[i][j]=triangle[i][j]+max(left,right)
    return max(dp[-1])
