import sys
input=sys.stdin.readline

n=int(input())
times=[tuple(map(int,input().split())) for _ in range(n)]
times.sort(key=lambda x:(x[1],x[0]))

# 1. 끝나는 시간의 오름차순
# 2. 시작하는 시간의 오름차순

cnt=1
end=times[0][1]
for i in range(1,n):
    if times[i][0]>=end:
        end=times[i][1]
        cnt+=1

print(cnt)
