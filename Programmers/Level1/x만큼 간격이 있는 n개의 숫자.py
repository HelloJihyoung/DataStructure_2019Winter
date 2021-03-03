# def solution1(x, n):
#     answer = []
#     cnt = 0
#     number = 0
#     while cnt < n:
#         number = number + x
#         answer.append(number)
#         cnt += 1
#     return answer

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append((i+1)*x)
    return answer
    
x = 2
n = 5
print(solution(x,n))