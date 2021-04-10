def solution(number, k):
    answer = []
    for i in range(len(number)):
        while answer and answer[-1] < number[i] and k > 0:
            answer.pop()
            k-=1
        answer.append(number[i])

    # 못뺏을 경우에는 슬라이싱해서 뒤에서 빼주기
    if k > 0 :
        answer = number[:-k]
    
    return ''.join(answer)

number = "4177252841"
print(solution(number, 4))