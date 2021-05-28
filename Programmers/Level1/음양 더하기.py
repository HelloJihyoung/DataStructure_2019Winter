def solution(absolutes, signs):
    sum = 0
    for i in range(len(signs)):
        if signs[i] == False:
            sum +=  -(absolutes[i])
        else:
            sum += absolutes[i]
    return sum


absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))


# def solution(absolutes, signs):
#     answer=0
#     for absolute,sign in zip(absolutes,signs):
#         if sign:
#             answer+=absolute
#         else:
#             answer-=absolute
#     return answer