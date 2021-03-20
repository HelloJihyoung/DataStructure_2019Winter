def solution(s):
    intHalf = int(len(s)/2)
    #print(len(s)//2)

    # 짝수일 경우
    if len(s):
        return s[intHalf-1]+s[intHalf]
    # 홀수일 경우
    else:
        return s[intHalf]
        
# def solution(s):
#     intHalf = int(len(s)/2)
#     halfLength = (len(s) / 2) % 1
#     if halfLength != 0:
#         return s[intHalf]
#     else:
#         return s[intHalf-1]+s[intHalf]

s = "qwer"
print(solution(s))