def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    soopo1 = [1,2,3,4,5] 
    soopo2 = [2,1,2,3,2,4,2,5] 
    soopo3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range (len(answers)):
        if answers[i] == soopo1[i%len(soopo1)]:
            cnt1 += 1
        if answers[i] == soopo2[i%len(soopo2)]:
            cnt2 += 1
        if answers[i] == soopo3[i%len(soopo3)]:
            cnt3 += 1

    count = [cnt1, cnt2, cnt3]
    best = max(cnt1, cnt2, cnt3)
    #print(best)

    for j in range (len(count)):
        if count[j] == best:
            print(j)
            answer.append(j+1)

    return answer

answers = [1,3,2,4,2]
print(solution(answers))