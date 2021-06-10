# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
from collections import Counter


def solution(clothes):
    temp = []

    for name, kind in clothes:  # 이름과 종류 따로 뽑음
        temp.append(kind)
        # print(temp)
    # print(temp)
    counter = Counter(temp)
    # print(counter['headgear'])
    # 의상 종류의 개수들 구함

    all_possible = 1  # 모든 경우의수 초기값(곱이므로 1)
    for key in counter:
        # print(counter[key])
        all_possible *= (counter[key] + 1)  # 각 종류의 +1을 곱하며 더한다

    return all_possible-1  # 아무것도 안입을 경우 빼기


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
