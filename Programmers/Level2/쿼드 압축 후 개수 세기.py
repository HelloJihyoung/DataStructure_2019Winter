def solution(arr):
    answer = [0, 0]
    row = len(arr)
    # 시작좌표 x, y, 행 개수
    def divide(x, y, n):
        # 행이 1개 일때, 즉 모든 수 같을때
        if n == 1:
            if arr[x][y]:
                return [0,1]
            else:
                return [1, 0]

        #13
        #24
        quadOne = divide(x, y, n // 2)
        quadTwo = divide(x + n // 2, y, n // 2)
        quadThree = divide(x, y + n // 2, n // 2)
        quadFour = divide(x + n // 2, y + n // 2, n // 2)
        print('-------one---------')
        print(quadOne)
        print('---------two--------')
        print(quadTwo)
        print('--------three---------')
        print(quadThree)
        print('---------four--------')
        print(quadFour)
        print('###############')

        # [0의 개수, 1의 개수]

        # 동일한 경우 1개로 취급
        if quadOne == quadTwo == quadThree == quadFour == [0,1] or quadOne == quadTwo == quadThree == quadFour == [1, 0]:
            return quadOne

        # 
        else: 
            return list(map(sum, zip(quadOne, quadTwo, quadThree, quadFour)))




    answer = divide(0, 0, row) 
    print(answer)
    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
solution(arr)