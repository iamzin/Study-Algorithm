from itertools import combinations
from collections import Counter

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]

# 코스요리: 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들로 구성
# 코스요리 메뉴는 최소 2가지 이상, 최소 2명 이상의 손님으로부터 주문

# ('X','Y') 랑 ('Y', 'X') 가 서로 다른 튜플이기 때문에 같은 조합이라고 맞춰줘야함


def solution(orders, course):
    answer = []
    course_map = {}  # key: 해당 코스, value: 해당 코스를 주문한 사용자 count
    course_max_list = []  # course의 코스 종류 개수에 해당되는 가장 많이 주문된 course의 주문 수 list

    for order in orders:
        for course_num in course:
            for comb in combinations(order, course_num):
                # 정렬을 통해 (x,y) 와  (y,x)를 같은 코스로 count하도록 함
                comb = tuple(sorted(list(comb)))
                print("comb: ", comb)
                if comb in course_map:
                    course_map[comb] += 1
                else:
                    course_map[comb] = 1
    print("course_map: ", course_map)

    for course_num in course:  # course 음식 개수: course_num
        max = 0
        # course_num에 해당하는 딕셔너리 키 possible_course
        # course_map의 키 (튜플 형태) 중 길이가 course_num인 경우들에 대해
        for possible_course in list(filter(lambda x: len(x) == course_num, course_map)):
            if max < course_map[possible_course]:
                max = course_map[possible_course]
        # 해당 course_num에 해당하는 것들 중 최다 주문 수를 course_max_list에 저장
        course_max_list.append(max)
    print("course_max_list: ", course_max_list)

    for i in range(len(course)):
        if course_max_list[i] < 2:
            continue
        for possible_course in list(filter(lambda x: len(x) == course[i], course_map)):
            # course_max_list의 값과 같은 value를 가진 course_map의 key를 answer에 저장
            if course_max_list[i] == course_map[possible_course]:
                # 튜플을 문자열로 변환할때는 join을 쓰자
                answer.append(''.join(possible_course))

    answer.sort()

    return answer


# Counter를 활용한 풀이
def solution2(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        print("order_combinations: ", order_combinations)

        most_ordered = Counter(order_combinations).most_common()
        print("most_ordered: ", most_ordered)
        result += [k for k, v in most_ordered if v >
                   1 and v == most_ordered[0][1]]
        print("result: ", result)

    return [''.join(v) for v in sorted(result)]


print(solution2(orders, course))
