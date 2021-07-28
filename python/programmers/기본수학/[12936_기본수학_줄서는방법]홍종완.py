# 줄서는 방법 - 기본수학 - 12936
# n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다.
# n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# 사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

# 제한사항
# n은 20이하의 자연수 입니다.
# k는 n! 이하의 자연수 입니다.

# 시간초과
# from itertools import permutations


# def solution(n, k):

#     arr = []
#     for i in range(1, n+1):
#         arr.append(i)

#     per_arr = list(permutations(arr, n))
#     print(per_arr)
#     # 정렬된 채로 나오는 듯
#     # per_arr.sort()

#     return list(per_arr[k-1])


# f(n) = f(n-1)!
# 한개에 몇개씩의 값이 있을지 알 수 잇음.
def fac_minus_one(num):
    answer = 1
    for i in range(1, num):
        answer *= i
    return answer

# print(fac_minus_one(5))


def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = fac_minus_one(n)  # 2
        index = k // temp  # k 번째
        k = k % temp  # k번 지나가고 남은 인덱스
        if k == 0:
            answer.append(numberList.pop(index-1))
        else:
            answer.append(numberList.pop(index))

        n -= 1

    return answer


print(solution(3, 5))
print(solution(20, 5))
