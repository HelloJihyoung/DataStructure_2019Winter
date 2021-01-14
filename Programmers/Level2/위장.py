#  첫번째 시도 : 단순 배열 사용 -> for문 너무 많이써서 효율성이 떨어진다!
#  def solution(clothes):
#     answer = 0
#     clothes_sort = []
    
#     for x, y in clothes:
#         clothes_sort.append(y)

#     clothes_sort = list(set(clothes_sort))
#     clothes_cnt = [0] * len(clothes_sort)

#     for i in range (len(clothes_sort)):
#         for j in range (len(clothes)):
#             if clothes_sort[i] == clothes[j][1]:
#                 clothes_cnt[i] += 1
#     answer = 1
#     for k in range(len(clothes_cnt)):
#          answer *= (clothes_cnt[k] + 1)

#     print(answer-1)    
      
#     return answer - 1

# 두번째 시도 : 딕셔너리 이용 (문제에서 주어진대로 hash를 이용함! 효율이 훨씬 좋아졌고 코드도 보기 좋아짐)
def solution(clothes):

    clothes_info = dict()

    for x, y in clothes:
        if y not in clothes_info:
            clothes_info[y] = 1
        else:
            clothes_info[y] += 1

    answer = 0
    
    for value in clothes_info.values():
        answer *= (value + 1)
        
    return answer -1
