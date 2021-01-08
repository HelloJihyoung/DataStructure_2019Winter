def solution(prices):

    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j  in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))

# 스택 큐 문젠데 이중 for문으로 풀었움.. 다시 할것임!!!!!!