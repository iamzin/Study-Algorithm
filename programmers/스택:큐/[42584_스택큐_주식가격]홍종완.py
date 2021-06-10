# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# def solution(prices):
#     answer = []

#     for i in range(len(prices)):
#         cnt = 0
#         for j in prices[i:]:
#             if prices[i] <= j:
#                 cnt += 1

#         answer.append(cnt-1)

#     return answer

# 시간초과
from collections import deque


def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in prices[i:]:
            if prices[i] <= j:
                cnt += 1
            else:
                cnt += 1
                break

        answer.append(cnt-1)

    return answer

# 슬라이싱 말고 범위지정해보기

# 스택 사용 -> 값이 아닌 가격의 인덱스를 스택에 넣었다가 뻄


def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:
            for j in stack[::-1]:  # 증가폭 -1 -> 새로 알게 됨
                if prices[i] < prices[j]:
                    answer[j] = i - j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    return answer


print(solution([1, 2, 3, 2, 3]))
# 테스트 케이스
print(solution([1, 2, 3, 2, 3, 1]))
# return -> 5 4 1 2 1 0


def solution(prices):
    answer = []

    prices = deque(prices)  # que로 캐스팅
    while prices:
        cnt = 0
        price = prices.popleft()  # First Out

        for i in prices:
            cnt += 1  # 카운팅
            if price > i:
                break

        answer.append(cnt)
    return answer
