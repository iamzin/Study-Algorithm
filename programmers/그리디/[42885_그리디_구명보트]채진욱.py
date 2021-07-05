from collections import deque

people = [70, 50, 80, 50]
limit = 100

# 40 <= 사람 몸무게 <= 240
# 40 <= 구명보트 limit <= 240

# 구명보트 한번에 최대 2명 밖에 못탐

# 보트 하나에 대해서 첫번째 사람은 false 인 사람부터 태움
# 태우고 True로 변경
# 두번째 사람은 (limit - 첫번째 사람)보다 작거나 같은 사람들 중 가장 무거운 사람을 태움
# 태우고 True로 변경
# 해당 보트 다 타면 다음 보트 + 1

# 못 풀었다...
# def solution(people, limit):
#     answer = 0
#     ontheboat = [False] * len(people)
#     people_cnt = len(people)
#     boat = limit

#     while False in ontheboat:
#         for i in range(len(people)):
#             if ontheboat[i] == False:
#                 for j in range(len(people)):
#                     if j != i and limit-people[i] >= people[j] and next_person <= people[j]:
#                         next_person = people[j]

#     # print("최소: ", min(people))
#     # print("해당 인덱스: ", people.index(min(people)))
#     return answer


# https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python
def solution2(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)
    while q:
        if len(q) >= 2:
            # 큐의 맨 앞(가장 무거운 사람) 과 맨 끝 (가장 가벼운 사람)의 합이 limit보다 작거나 같으면
            if q[0] + q[-1] <= limit:
                q.pop()  # 맨 앞 pop
                q.popleft()  # 맨 뒤 pop
                boat += 1
            # 큐의 맨 앞(가장 무거운 사람) 과 맨 끝 (가장 가벼운 사람)의 합이 limit보다 크면
            elif q[0] + q[-1] > limit:
                q.pop()  # 맨 앞 pop
                boat += 1
        else:
            q.pop()
            boat += 1
    return boat


def solution3(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer  # 사람 수에서 짝지어지는 수를 빼면 보트 개수


solution2(people, limit)
