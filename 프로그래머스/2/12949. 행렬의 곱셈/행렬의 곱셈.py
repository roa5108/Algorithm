def solution(arr1, arr2):
    n, m, k = len(arr1), len(arr2), len(arr2[0])
    answer = [[0]*k for _ in range(n)]
    
    for a in range(n):
        for b in range(k):
            for c in range(m):
                answer[a][b]+=arr1[a][c]*arr2[c][b]
    return answer