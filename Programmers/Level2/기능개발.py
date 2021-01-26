import math

def solution(progresses, speeds):
    term = []
    answer = []

    for i in range (len(progresses)):
        cal = math.ceil(float(100-progresses[i]) / speeds[i])
        term.append(cal)

    print(term)
    # [5, 10, 1, 1, 20, 1]
    cnt = 1
    while len(term) > 0:
        front = term.pop(0)
        for i in term:            
            if front > i:
                cnt += 1
                break
            else:
                if len(term) == 1 and front < i:
                    cnt += 1
                    break
                answer.append(cnt)
                cnt = 1    
        

    print(answer)
    return answer



progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

solution(progresses, speeds)