def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        arr1Bin = list(map(int, str(format(arr1[i], 'b').zfill(n))))
        arr2Bin = list(map(int, str(format(arr2[i], 'b').zfill(n))))

        toBin = []
        i = 0
        while i < n:   
            if arr1Bin[i] == 0 and arr2Bin[i] == 0:
                toBin.append(' ')
            else:
                toBin.append('#')
            i+=1

        toBin2 = "".join(toBin)
        answer.append(toBin2)

    return answer

# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         a = str(bin(arr1[i]|arr2[i])[2:]).rjust(n,'0').replace('1','#').replace('0',' ')
#         answer.append(a)
#     return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
solution(n, arr1, arr2)