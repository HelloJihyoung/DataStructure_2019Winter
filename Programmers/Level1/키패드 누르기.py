def solution(numbers, hand):
    answer = ''
    # 0 1 2 3 4 5 6 7 8 9 10* 11#
    position = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2], [3,0], [3,2]]
    hand = 'R' if hand == 'right' else 'L'
    lastLeft = 10
    lastRight = 11
    distanceL = 0
    distanceR = 0
    for i in numbers:
        if i in [1,4,7, "*"]:
            answer += 'L'
            lastLeft = i
        elif i in [3,6,9, "#"]:
            answer += 'R'
            lastRight = i
        elif i in [2,5,8,0]:
            distanceL = abs(position[i][0]-position[lastLeft][0]) + abs(position[i][1]-position[lastLeft][1])
            distanceR = abs(position[i][1]-position[lastRight][1]) + abs(position[i][0]-position[lastRight][0])
            if  distanceL > distanceR:
                answer += 'R'
                lastRight = i
            elif distanceL < distanceR:
                answer += 'L'
                lastLeft = i
            elif distanceL == distanceR:
                answer += hand
                if hand == 'R':
                    lastRight = i
                if hand == 'L':
                    lastLeft = i
    return answer

numbers = [4,5,0]
hand = "right"
print(solution(numbers,hand))