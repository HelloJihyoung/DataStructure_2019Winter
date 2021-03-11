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
        # else:
        #     pass
        
    
    # for mes in record: 
    #     if mes.split(' ')[0] == 'Enter': 
    #         # userdict[mes.split(' ')[1]] + '님이 들어왔습니다.' 이런식으로 해도 가능 
    #         answer.append("{}님이 들어왔습니다.".format(logInfo[mes.split(' ')[1]]))
    #     elif mes.split(' ')[0] == 'Leave': 
    #         answer.append("{}님이 나갔습니다.".format(logInfo[mes.split(' ')[1]]))
    #     else:
    #         pass

    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))