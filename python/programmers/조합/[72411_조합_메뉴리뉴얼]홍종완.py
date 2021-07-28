# 메뉴 리뉴얼 - 조합 - 72411

# 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders,
# "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때,
#  "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
from itertools import combinations


def my_counter(iterate):
    dict = {}

    for element in iterate:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # sort를 왜할까..
            com = combinations(sorted(order), c)
            temp += com
        # print(temp)
        cnt = my_counter(temp)
        # print(cnt)

        # 최소 2개 이상
        if cnt and max(cnt.values()) > 1:
            max_cnt = max(cnt.values())
            for key, value in cnt.items():
                if cnt[key] == max_cnt:
                    answer.append(''.join(key))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
