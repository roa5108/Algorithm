matrix=[list(map(int,input().split())) for _ in range(9)]
max=-1
max_row,max_col=0,0

for i in range(9):
    for j in range(9):
        if matrix[i][j]>max:
            max=matrix[i][j]
            max_row=i
            max_col=j

print(max)
print(max_row+1,max_col+1,end=" ")