# 
# def solution_(people, limit):
#     answer = 0
    
#     people.sort()
#     i = 0 
#     while True:
#         if i == len(people) - 1:
#             answer += 1
#             break
#         elif people[i] + people[i+1] <= limit:
#             answer += 1
#             i += 2
#         elif people[i] <= limit and people[i+1] + people[i] > limit:
#             answer += 1
#             i += 1
        
#     print(answer)
#     return answer


def solution(people, limit):
    answer = 0
    
    people.sort()

    # 양끝에서부터 확인
    i = 0 
    j = len(people) - 1

    # 중심에 도달할때까지 반복
    while i <= j:
        # max 값을 cnt 한번 해주고 시작
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer

people = [30,40,50,60,70,80]
limit = 100
solution(people, limit)