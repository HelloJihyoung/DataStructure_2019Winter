def solution(s):

    flag = 0
    for num in s:    
        if num == "(":
            flag += 1
        else:
            flag -= 1
        
        if flag < 0:
            return False

    if flag == 0:
        return True

    return False

# 같은 방법을 Queue를 이용하여 푼 문제!
# def solution(s):
#     answer = True
#     Queue = []
#     for i in s: 
#         if i == '(': Queue.append('(')
#         else: 
#             try: Queue.pop() 
#             except: return False
#     if len(Queue) == 0: return True
#     else: return False


s = "(()("

print(solution(s))