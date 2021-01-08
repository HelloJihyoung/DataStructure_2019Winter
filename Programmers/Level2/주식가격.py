# # 첫번째 시도 : 단순 이중for문 사용
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j  in range(i+1, len(prices)):
#             answer[i] += 1
#             if prices[i] > prices[j]:
#                 break

#     return answer


# # 두번째 시도 : 스택 큐 이용 -> 시간 초과
# # def solution(prices):

# #     answer = []
# #     while prices:
# #         frontPop = prices.pop(0)
# #         cnt = 0
# #         for i in prices:
# #             if frontPop > i:
# #                 cnt += 1
# #                 break
# #             else:
# #                 cnt += 1
# #         answer.append(cnt)

# #     return answer


# # 세번째 시도 : 덱 이용 / 스택 큐에서는 덱을 이용하는것이 빠르다
# # pop(0) 은 O(n)이고 popleft는 O(1) 이기 때문이지

import collections

def solution(prices):

    answer = []
    prices = collections.deque(prices)
    while prices:
        frontPop = prices.popleft()
        cnt = 0
        for i in prices:
            if frontPop > i:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)

    return answer


prices = [4,3,2,1,2,3]
print(solution(prices))
