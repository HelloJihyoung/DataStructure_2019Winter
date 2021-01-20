from string import ascii_uppercase


def solution(name):
    alpha = list(ascii_uppercase)
    answer = 0

    for i in range(len(name)):
        if name.count('A') == len(name):
            return answer
        else:
            MIN = min(alpha.index(name[i]), 27-(alpha.index(name[i])))
            print(MIN)
            answer += MIN

    return answer


name = "ZZZ"
print(solution(name))


# 26-alpha.index 해야지 원래는 그 자리 인덱스가 나오는데
# 27을 해준 이유는 조이스틱 마지막으로 이동시키는 수 포함시키기 위해서
