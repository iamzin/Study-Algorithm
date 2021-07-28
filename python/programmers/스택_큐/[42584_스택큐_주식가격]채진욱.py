# 내 풀이
# 스택 문제이지만 브루트포스로 풀어버렸다.
# 틀리진 않았지만 시간 복잡도가 O(n^2)라서 스택으로 푸는 방법도 알아야 한다.

prices = [3, 1, 4, 5, 2]


def solution(prices):
    answer = []

    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    answer.append(0)

    return answer


print(solution(prices))