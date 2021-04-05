def solution(a, b):
    product = [x*y for x,y in zip(a,b)]
    return sum(product)