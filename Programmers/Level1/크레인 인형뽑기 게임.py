def solution(board, moves):
    count = 0
    basket = []
    for i in moves:
        for j in range (len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        count += 2
                break

    return count

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))