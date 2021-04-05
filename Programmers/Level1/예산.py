def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

solution([1,3,2,5,4], 9)