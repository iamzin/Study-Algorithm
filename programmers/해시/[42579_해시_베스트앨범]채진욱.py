genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 900, 900, 2500]


def solution(genres, plays):
    answer = []
    dic = {}
    genre_list = []

    # 해쉬 테이블 구성 key: 장르, value: [(고유번호, 재생횟수)]
    for i in range(len(plays)):
        if genres[i] in dic:
            dic[genres[i]].append((i, plays[i]))
        else:
            dic[genres[i]] = [(i, plays[i])]

    # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    # print(dic)

    for key in dic:
        genre_played = 0
        # 다중 정렬 => 먼저 x[1] 내림차순 정렬 후, x[0] 오름차순 정렬
        dic[key].sort(key=lambda x: (-x[1], x[0]))

        # 장르에 해당하는 노래들의 재생횟수를 더함
        for val in dic[key]:
            genre_played += val[1]

        # 장르 재생 횟수를 저장하는 genre_list 구성
        genre_list.append((key, genre_played))

    genre_list.sort(key=lambda x: -x[1])  # 장르 재생 횟수 내림차순으로 정렬

    # print(dic)
    # print(genre_list)  # [('pop', 3100), ('classic', 1450)]

    for genre in genre_list:
        if len(dic[genre[0]]) == 1:  # 장르에 속한 곡이 하나인 경우
            answer.append(dic[genre[0]][0][0])
        else:
            answer.append(dic[genre[0]][0][0])
            answer.append(dic[genre[0]][1][0])

    return answer


print(solution(genres, plays))
