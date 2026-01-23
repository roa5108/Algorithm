def solution(k, dungeons):
    visited = [False]*len(dungeons)
    
    def dfs(cur, cnt):
        maxCnt = cnt
        for i, (required, cost) in enumerate(dungeons):
            if not visited[i] and cur>=required:
                visited[i] = True
                maxCnt = max(maxCnt, dfs(cur-cost, cnt+1))
                visited[i] = False
        return maxCnt
                
    return dfs(k, 0)
    

