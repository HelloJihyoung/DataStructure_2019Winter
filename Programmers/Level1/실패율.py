# 다시 짜기~~!
#from collections import Counter
def solution(N, stages):
    answer = []
    countStage = {i : 0 for i in range (1, N+1)}
    #countStage = Counter(stages)
    people = len(stages)
    
    #print(Counter(sorted(stages)))
    for i in range(1, N+1):
        # 이부분이 오래걸려!!! count < counter
        countStage[i] = stages.count(i)
    
    for key, value in countStage.items():
        try:
            answer.append([key, value / people])
        except:
            answer.append([key, 0])
        people = people - value

    new = sorted(answer, key=lambda answer: answer[1], reverse=True)

    return [i[0] for i in new]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
