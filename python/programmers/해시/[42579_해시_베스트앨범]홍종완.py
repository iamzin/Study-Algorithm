# 베스트 앨범 - 해시 - 42579
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

from collections import defaultdict


def solution(genres, plays):
    answer = []

    # dictionary에 값 넣기(기본)
    genres_dict = {}
    total_dict = {}

    for i in range(len(genres)):
        # 해당 키 있는지 먼저 검사, 있으면 +=
        if genres[i] in genres_dict:
            genres_dict[genres[i]] += plays[i]
            total_dict[genres[i]].append((plays[i], i))
            # total_dict 는 튜플로 재생횟수,인덱스 값을 저장해준다
        # 없으면 그냥넣고
        else:
            genres_dict[genres[i]] = plays[i]
            total_dict[genres[i]] = [(plays[i], i)]

    # # defaultdict 사용하는 방법
    # genres_dict = defaultdict(lambda: 0)
    # total_dict = defaultdict(lambda: [])

    # for i in range(len(genres)):
    #     genres_dict[genres[i]] += plays[i]
    #     total_dict[genres[i]].append((plays[i], i))

    print('정렬 전')
    print(genres_dict)
    print(total_dict)

    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)
    # dictionary의 키,밸류 쌍 얻기 - items()
    # lambda -> 밸류 기준 정렬

    for i in total_dict:
        total_dict[i] = sorted(
            total_dict[i], key=lambda x: x[0], reverse=True)[:2]  # 2개까지만

    print('정렬 후')
    print(genres_dict)
    print(total_dict)

    while len(genres_dict) > 0:
        genre_max = genres_dict.pop(0)
        print(genre_max)
        for t in total_dict:
            if t == genre_max[0]:
                # 문제 조건, 1개 이상일 경우 두개만 담아준다
                if len(total_dict[t]) > 1:
                    answer.append(total_dict[t][0][1])
                    answer.append(total_dict[t][1][1])
                # 하나일 경우
                else:
                    answer.append(total_dict[t][0][1])

    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))

# 참고
# https://velog.io/@younge/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-%ED%95%B4%EC%8B%9C
