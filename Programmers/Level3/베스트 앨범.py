def solution(genres, plays):
    answer = []

    # 장르 : 총 횟수
    totalPlay = {}

    # 장르:(횟수, index)
    totalPlayList = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        totalPlay[genre] = totalPlay.get(genre, 0) + play
        totalPlayList[genre] = totalPlayList.get(genre, []) + [ (play, i) ]

    
    #장르별 재생횟수 내림차순 정렬
    totalPlay = sorted(totalPlay.items(), key=lambda x : x[1], reverse=True)
    
    for i, j in totalPlay:
        totalPlayList[i] = sorted(totalPlayList[i], key = lambda x : (-x[0], x[1]))
        answer += [ index for (play, index) in totalPlayList[i][:2]]        

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))