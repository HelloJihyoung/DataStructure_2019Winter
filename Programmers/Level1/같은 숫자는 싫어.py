# def solution(arr):
#     answer = []
#     for i in arr:
#         if answer[-1:] == [i]:
#             continue
#         answer.append(i)
#     return answer

# 효율성 거의 3배? 증가 -> 슬라이싱 때문인듯
def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)
    return answer