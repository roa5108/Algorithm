import heapq

def solution(jobs):
    jobs.sort()
    heap=[]
    time,end,idx = 0,0,0
    cnt=len(jobs)
    answer=0
        
    while idx<cnt or heap:
        while idx<cnt and jobs[idx][0]<=end:
            start, duration = jobs[idx]
            heapq.heappush(heap,(duration,start))
            idx+=1
            
        if not heap:
            end=jobs[idx][0]
            continue
            
        duration,start=heapq.heappop(heap)
        end+=duration
        answer+=end-start
        
    return answer//cnt
            