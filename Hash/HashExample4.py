def solution(genres, plays):
    answer = []
    dicGenre = {}

    index = 0
    for g in genres:
        if g in dicGenre:
            dicGenre[g].append({index : plays[index]})
        else:
            dicGenre[g] = [{index : plays[index]}]
        index = index+1

    print(dicGenre)

    for v in dicGenre.values():
        for item in v:

            print(item)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

answer = solution(genres, plays)

print(answer)