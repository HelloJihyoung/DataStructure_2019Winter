def solution(n):
    answer = ''
    # 몫과 나머지
    quotient = 1
    remainder = 1
    # 나머지에따라 값 바꿔주기 위한 dictionary
    country = {1: "1", 2: "2", 0: "4"}
    # 몫이 0일때까지 반복
    while quotient != 0:
        quotient = n // 3
        remainder = n % 3
        # 나머지가 0일 경우에는 몫에서 1을 빼준다
        if remainder == 0:
            quotient -= 1
        
        # 숫자 갱신
        n = quotient

        # 앞부분에 숫자를 붙여가며 만든다
        answer = country[remainder] + answer

    return answer

n = 10
print(solution(n))