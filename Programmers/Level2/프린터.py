def solution(priorities, location):

    answer = 0
    maxP = max(priorities)

    while True:
        frontPop = priorities.pop(0)
        if  frontPop == maxP:
            answer+=1
            if location == 0:
                break
            else:
                location -= 1
            maxP = max(priorities)
        else:
            priorities.append(frontPop)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1 

    return answer

# def solution(priorities, location):

#     f_loc = []
#     loc = [i for i in range(len(priorities))]

#     while len(priorities)>0 :
#         if priorities[0] == max(priorities): # max 일때
#             f_loc.append(loc.pop(0))
#             priorities.pop(0)
#         else: #max가 아닐때, 다시 priorities 마지막으로 감.
#             priorities.append(priorities.pop(0))
#             loc.append(loc.pop(0))

#     return f_loc.index(location) + 1


# def solution(priorities, location):

#     loc = [i for i in range(len(priorities))]

#     while len(priorities) > 0:
        
#         if priorities[0] == max(priorities):  # max 일때
#             loc.append(loc.pop(0))
#             priorities.pop(0)
#             loc.remove(max(loc))
#         else:  # max가 아닐때, 다시 priorities 마지막으로 감.
#             priorities.append(priorities.pop(0))
#             loc.append(loc.pop(0))

#     return loc.index(location)+1


location = 0
priorities = [1, 2, 3, 4, 5, 6]
print(solution(priorities,location))
