def solution(brown, yellow):
    answer = []
    decimal = []
    #decimal_back =[]
    
    
    for i in range(1, int(yellow**(1/2)) + 1): 
        if yellow % i == 0:
            decimal.append(i)
            if (i != (yellow // i)): 
                #decimal_back.append(yellow//i)
                decimal.append(yellow//i)

    #decimal = (decimal + decimal_back[::-1])[::-1]
    decimal.sort

    for i in range(len(decimal)):

        check = (decimal[i] * 2) + (yellow/decimal[i] * 2) + 4

        if brown == check:
            answer.append(decimal[i] + 2)
            answer.append(yellow/decimal[i] +2)
            break

    return answer