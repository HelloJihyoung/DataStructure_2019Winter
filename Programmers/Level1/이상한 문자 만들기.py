def solution(s):
    answer = []
    split = s.split(' ')
    for i in split:
        forAnswer = ""
        for j in range(len(i)):
            if j % 2 == 0:
                forAnswer += i[j].upper()
            else:
                forAnswer += i[j].lower()
        answer.append(forAnswer)
    
    return " ".join(answer)

s = "try hello world"
print(solution(s))