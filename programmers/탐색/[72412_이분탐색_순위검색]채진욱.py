from itertools import combinations
from bisect import bisect_right, bisect_left

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


def solution(info, query):  # 내 풀이: 정확성 테스트는 통과, 효율성 테스트는 실패
    answer = [0] * len(query)

    member = []  # 각 지원자 정보 담는 리스트 ex) [java, backend, junior, pizza, 150]
    info_list = [member] * len(info)  # member를 담는 이중리스트

    # info에서 정보 파싱
    for i in range(0, len(info)):
        info_split = info[i].split(" ")
        for j in range(0, 5):
            if j == 4:
                member.append(int(info_split[j]))
                break
            member.append(info_split[j])
        info_list[i] = member
        member = []

    query_char = []  # 각 쿼리의 정보 담는 리스트
    query_list = [query_char] * len(query)  # query_char를 담는 이중리스트

    for i in range(0, len(query)):
        query_split = query[i].split(" and ")
        for j in range(0, 4):
            if j == 3:
                foodAndScore = query_split[j].split(" ")
                query_char.append(foodAndScore[0])
                query_char.append(int(foodAndScore[1]))
                break
            query_char.append(query_split[j])
        query_list[i] = query_char
        query_char = []

    # info_list -> 이중 포문써서 각 멤버의 특성으로 접근해서 query와 일치하면 1, 일치하지 않으면 0
    # 특성 값이 - 일 경우 -> 현재 특성은 넘어감

    for i in range(len(query)):
        for j in range(len(info)):
            for k in range(5):
                if query_list[i][k] == '-':
                    continue
                elif k == 4:
                    if info_list[j][4] >= query_list[i][4]:
                        answer[i] += 1
                elif info_list[j][k] != query_list[i][k]:
                    break
    return answer


# 해쉬테이블
# combination(조합)
# 이분탐색 (lower bound)

# 멤버의 info에서 해당가능한 모든 query case를 구하는 함수
# temp = ["java", "backend", "junior", "pizza", "150"]
def make_all_cases(temp):
    cases = []
    for i in range(5):
        # print(list(combinations([0, 1, 2, 3], i)))
        # temp의 index 인 0,1,2,3 중 0,1,2,3,4개 씩 뽑는다.
        for combination in combinations([0, 1, 2, 3], i):
            case = ''
            for idx in range(4):
                if idx not in combination:
                    case += temp[idx]  # javabackendjuniorpizza 이런 식으로 저장
                else:
                    case += '-'
            cases.append(case)
            # print(cases)
    return cases


# lower_bound 구현
# taget보다 큰 값의 최소 인덱스를 찾는 과정
def get_lower_bound(target, array):
    current_min = 0
    # 아예 target이 array 점수들 보다 큰 경우도 있기때문에 len(array)-1 대신 len(array)로 지정
    current_max = len(array)

    while current_min < current_max:
        current_guess = (current_min + current_max) // 2
        if array[current_guess] >= target:
            # array[current_guess]가 target보다 큰거나 같은 경우는 더이상 탐색할 필요가 없으므로 최댓값(current_max)을 시도값(current_guess)으로 변경
            current_max = current_guess
        else:
            # array[current_guess]가 target보다 작은 경우는 알고자하는 범위가 아니므로 최소값(current_min)을 시도값(current_guess) + 1 로 변경
            current_min = current_guess + 1

    return current_max


def solution2(info, query):
    answer = []
    # 해쉬 테이블 (key-value): key에는 query case, value에는 list 형태로 query case에 해당하는 유저의 점수 받음
    all_cases_from_users = {}

    for user_info in info:
        # split 안에 아무것도 없으면 그냥 공백 기준으로 자름 -> ["java", "backend", "junior", "pizza", "150"]
        user_info_array = user_info.split()
        all_cases_from_user = make_all_cases(user_info_array)
        for case in all_cases_from_user:
            if case not in all_cases_from_users.keys():  # case가 해쉬테이블의 key 들 중에 없다면 (즉, case가 해당하는 key를 새로 만들어줌)
                # all_cases_from_users라는 해쉬 테이블에 value 값으로 점수를 넣음
                all_cases_from_users[case] = [int(user_info_array[4])]
            else:  # case가 해쉬테이블에 존재하므로 value만 list에 추가
                all_cases_from_users[case].append(int(user_info_array[4]))

    for key in all_cases_from_users.keys():  # 이분탐색(lower_bound)를 위해 정렬
        all_cases_from_users[key].sort()

    for query_info in query:
        query_info_array = query_info.split()
        case = query_info_array[0] + query_info_array[2] + \
            query_info_array[4] + query_info_array[6]  # 공백, and 빼고 실제 정보만 빼옴
        if case in all_cases_from_users.keys():
            # query case에 해당되는 유저들의 점수 list
            target_users = all_cases_from_users[case]
            answer.append(
                len(target_users) -
                bisect_left(target_users, int(
                    query_info_array[7]))  # 이진탐색 파이썬 모듈
                # get_lower_bound(int(query_info_array[7]), target_users)
            )
        else:  # case에 해당하는 유저가 없는 경우
            answer.append(0)

    return answer


print(solution2(info, query))
# make_all_cases(["java", "backend", "junior", "pizza", "150"])
