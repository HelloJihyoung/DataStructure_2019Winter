# def solution(scoville, K):
#     answer = 0
    
#     while min(scoville) < K:
#         if len(scoville) == 0:
#             return -1
#         scoville.sort()
#         scoville.append(scoville[0] + scoville[1] * 2)
#         scoville.pop(0)
#         scoville.pop(0)

#         answer += 1
#     return answer

# 우선 순위 큐
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)# 기존 리스트를 heapq 로 변환
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer

scoville = [1,1,100]
print(solution(scoville, 7))