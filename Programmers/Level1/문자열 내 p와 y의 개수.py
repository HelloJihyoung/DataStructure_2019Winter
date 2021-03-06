# def solution(s):
#     s = s.upper()
#     cnt = 0
#     for i in range(len(s)):
#         if s[i] == "P":
#             cnt += 1
#         elif s[i] == "Y":
#             cnt -= 1

#     if cnt == 0:
#         return True
#     else:
#         return False


def solution(s):

    if s.upper().count("P") == s.upper().count("Y"):
        return True
    else:
        return False

s = "pPoooyY"
print(solution(s))