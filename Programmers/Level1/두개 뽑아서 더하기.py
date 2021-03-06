def solution(numbers):
    answer = []
    numbers.sort()
    print(numbers)
    for i in numbers:
        for j in numbers:
            if i + j not in answer:
                answer.append(i+j)
    return answer


numbers = [2,1,3,4,1]
print(solution(numbers))