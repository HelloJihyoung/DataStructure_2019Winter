def solution(n):

    # n을 2진수로 변환 후 1의 개수 세기
    cntBinary = bin(n).count('1')
    nextBig = n+1
    while True:
        if bin(nextBig).count('1') == cntBinary:
            return nextBig
        nextBig += 1


n = 78
print(solution(n))

