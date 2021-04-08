def solution(n):
    answer = ''
    # 몫과 나머지
    quotient = 1
    remainder = 1
    country = {1: "1", 2: "2", 0: "4"}
    while quotient != 0:
        quotient = n // 3
        remainder = n % 3
        if remainder == 0:
            quotient -= 1
        
        n = quotient
        answer = country[remainder] + answer

    return answer

n = 10
print(solution(n))