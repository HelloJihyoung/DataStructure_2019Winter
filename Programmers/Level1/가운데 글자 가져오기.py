def solution(s):
    intHalf = int(len(s)/2)
    if len(s):
        return s[intHalf-1]+s[intHalf]
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