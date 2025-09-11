import sys
input = sys.stdin.readline

# 스도쿠 보드 입력
board = [list(map(int, input().strip())) for _ in range(9)]

# 빈칸 좌표 저장
empties = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def check(x, y, n):
    # 행 체크
    if n in board[x]:
        return False
    # 열 체크
    if n in [board[i][y] for i in range(9)]:
        return False
    # 3x3 박스 체크
    sx, sy = (x//3)*3, (y//3)*3
    for i in range(sx, sx+3):
        for j in range(sy, sy+3):
            if board[i][j] == n:
                return False
    return True

def dfs(idx):
    if idx == len(empties):   # 다 채우면 출력
        for row in board:
            print(''.join(map(str, row)))
        sys.exit(0)  # 정답 여러 개일 수 있으니 바로 종료
    x, y = empties[idx]
    for num in range(1, 10):
        if check(x, y, num):
            board[x][y] = num
            dfs(idx+1)
            board[x][y] = 0

dfs(0)