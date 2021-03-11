def solution(record):
    answer = []
    logInfo = {}
    
    for i in record:
        arrSplit = i.split(" ")
        if arrSplit[0] == "Enter" or arrSplit[0] == "Change":
            logInfo[arrSplit[1]] = arrSplit[2]

    for i in record:
        arrSplit = i.split(" ")
        if arrSplit[0] == "Enter":
            answer.append(logInfo[arrSplit[1]] + '님이 들어왔습니다.' )
        elif arrSplit[0] == "Leave":
            answer.append(logInfo[arrSplit[1]] + '님이 나갔습니다.' )
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))