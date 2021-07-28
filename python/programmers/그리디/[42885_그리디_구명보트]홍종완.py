# 구명보트 - 그리디 - 42885

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
#  모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 두명만 태울 수 있는 조건과 testcase2를 못함
# def solution(people, limit):
#     answer = 1
#     people.sort()

#     # 제한과 비교할 temp
#     temp = people[0]

#     # 1부터 N까지
#     for p in range(1, len(people)):
#         # 계속 더해갈 것
#         temp += people[p]
#         # 비교했는데 넘치면
#         if temp > limit:
#             # 횟수 증가
#             answer += 1
#             # temp 초기화(해당 사람으로)
#             temp = people[p]

#     return answer


# testcase2를 생각하자
from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()
    people = deque(people)
    while len(people) > 0:
        if len(people) == 1:  # 혼자 남았을 경우에는 아래식을 하면 범위 초과 에러
            return answer + 1
        ddung = people.pop()  # 제일 무거운 사람 뺌
        if limit >= ddung + people[0]:  # 제일 무거운사람하고 가벼운사람 더해서 limit보다 작거나 같으면
            people.popleft()  # 제일 가벼운 사람도 뺌
            answer += 1  # answer += 1
        else:  # 리밋보다 크면
            answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
# testcase2
print(solution([40, 40, 40, 40, 60, 60, 60, 60], 100))
print(solution([40, 50, 60, 90], 100))

# 신기한 풀이..


def solution(people, limit):
    answer = 0
    people.sort()

    # a와 b는 인덱스로
    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            # 성립할때만 a, answer 증가
            a += 1
            answer += 1
        # 턴때마다 b 감소
        b -= 1
    return len(people) - answer  # len - answer
