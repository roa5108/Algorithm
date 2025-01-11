n,m=map(int,input().split())
matrices=[]

for i in range(2):
    matrix=[list(map(int,input().split())) for _ in range(n)]
    matrices.append(matrix)

for j in range(n):
    for k in range(m):
        matrices[0][j][k]+=matrices[1][j][k]
        print(matrices[0][j][k],end=" ")
    print()