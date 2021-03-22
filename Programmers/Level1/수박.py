# ( if가 참일때 값 ) if (조건문) else (if가 false일때 값)
def solution(n):
    # return ('수박'*n) [:n] -> 이게 더 느림
    return ('수박'* int(n/2) ) if n % 2 == 0 else ('수박'* int(n/2) ) + '수'

n = 3
print(solution(n))