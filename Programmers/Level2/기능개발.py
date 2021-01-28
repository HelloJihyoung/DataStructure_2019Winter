import math


def solution(progresses, speeds):
    term = []
    answer = []

    for i in range(len(progresses)):
        cal = math.ceil(float(100-progresses[i]) / speeds[i])
        term.append(cal)

    print(term)
    # [5, 10, 1, 1, 20, 1]
    cnt = 1
   
    for i in range(1,  len(term)):
        if term[i-cnt] >= term[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    print(answer)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

solution(progresses, speeds)
