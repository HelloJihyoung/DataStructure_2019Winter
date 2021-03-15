def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

def solution(a, b):
    answer = 0
    for item in range(min(a,b), max(a,b)+1):
        answer += item
    return answer


print(solution(3, 5))