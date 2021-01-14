# def solution(clothes):
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

#clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
solution(clothes)