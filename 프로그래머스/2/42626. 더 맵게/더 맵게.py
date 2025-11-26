import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        a=heapq.heappop(scoville) #힙의 최솟값
        b=heapq.heappop(scoville) #다음 최솟값. 힙의 특성으로, pop되고 바로 다음 최솟값이 루트가 되기 때문
        heapq.heappush(scoville, a+b*2)
        cnt+=1
        
    return cnt