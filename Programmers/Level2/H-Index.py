def solution_(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        print(i+1, citations[i])   
        if citations[i] < i+1:    
            answer = i
            break
        else:
            answer = len(citations)

    return answer

# 훨씬 빠르군!!!
def solution(citations):
    answer = 0
    citations.sort()
    index = len(citations)
    print(citations)

    for i in range(index):  
        if citations[i] >= index-i:
            answer = index-i
            break

    return answer

citations = [3, 0, 6, 1, 5]
solution(citations)