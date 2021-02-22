def solution(x):
    sumOf = sum(map(int, str(x)))
    if x % sumOf == 0:
        return True
    else:
        return False
