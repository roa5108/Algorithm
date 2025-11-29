def solution(triangle):
    answer = 0
    dp=[[0]*len(row) for row in triangle]
    dp[0][0]=triangle[0][0]
    n=len(triangle)
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j>0:
                left=dp[i-1][j-1]
            else:
                left=0
                
            if j<len(triangle[i-1]):
                right=dp[i-1][j]
            else:
                right=0
                
            dp[i][j]=max(left,right)+triangle[i][j]
    return max(dp[-1])