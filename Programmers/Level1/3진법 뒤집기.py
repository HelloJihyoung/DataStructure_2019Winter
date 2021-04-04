def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n):
    reverse = convert(n, 3)[::-1]
    answer = int(reverse, 3)
    return answer

n = 45
print(solution(n))