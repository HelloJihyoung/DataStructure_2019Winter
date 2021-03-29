import re
def solution(dartResult):
    answer = [0, 0, 0]
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    
    find = re.compile('(\d+)([SDT])([*#])?')
    score = find.findall(dartResult)    
    for i in range(len(score)):
        if score[i][2] == '*' and i > 0:
            answer[i-1] *= 2
        answer[i] = int(score[i][0]) ** bonus[score[i][1]] * option[score[i][2]]

    return sum(answer)

dartResult = "1S2D*3T"
print(solution(dartResult))