def solution(s, n):
    a = list(s)
    for i in range(len(s)):
        if ord(a[i]) == 32:
            a[i] = " "
        elif a[i].isupper():
            a[i] = chr((ord(a[i]) + n - 65) % 26 + 65)
        elif a[i].islower():
            a[i] = chr((ord(a[i]) + n - 97) % 26 + 97)

    return "".join(a)

s = "a B z"
n = 4
print(solution(s, n))

# import string
# def solution(s, n):
#     answer = ''
#     alpha = list(string.ascii_lowercase)
#     ALPHA = list(string.ascii_uppercase)
   
#     for i in s:
#         #chr(ord(i) + n)
                
#         if ord(i) == 32:
#             answer.append(" ")

#         # 대문자인 경우
#         elif ord(i) <= 90:
#             if ALPHA.index(i) + n > 25:
#                 index = ALPHA.index(i) + n - 25
#                 answer.append(index)
#             else:
#                 answer.append(ALPHA[ALPHA.index(i) + n])
#         # 소문자인 경우
#         else:
#             if alpha.index(i) + n > 25:
#                 index = alpha.index(i) + n - 25
#                 answer.append(index)
#             else:
#                 answer.append(alpha[alpha.index(i) + n])


#         #print(chr(ord(i) + n))
#     return answer

