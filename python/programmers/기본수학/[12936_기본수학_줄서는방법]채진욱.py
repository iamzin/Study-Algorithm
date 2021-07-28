from itertools import permutations
import math

n = 3
k = 5

# 정확성: 63.2
# 효율성: 0.0
# 합계: 63.2 / 100.0 -> 시간초과


def solution(n, k):
    n_list = list((i for i in range(1, n+1)))
    order_list = []

    for perm in permutations(n_list, len(n_list)):
        order_list.append(perm)

    order_list.sort(key=lambda x: (x[0], x[1], x[2]))
    print(order_list)

    for i in range(0, len(order_list)):
        if i == k-1:
            return list(order_list[i])


def solution2(n, k):  # https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-Python
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = math.factorial(n) // n  # 한개에 몇개씩의 값이 있을지 알 수 있음
        index = k // temp  # 1~n 중 어떤 걸로 시작하는 지 알 수 있음
        k = k % temp  # ?로 시작하는 수 중에서 몇 번째 인지
        print("temp: ", temp)
        print("index: ", index)
        print("k: ", k)
        if k == 0:  # 그 이전 수로 시작하는 수들 중 마지막 수가 들어가야함
            answer.append(numberList.pop(index-1))
            print("answer: ", answer)
        else:  # ?로 시작하는 수 중 indx 번째
            answer.append(numberList.pop(index))
            print("answer: ", answer)
        n -= 1
    print("answer: ", answer)
    return answer


print(solution2(n, k))
