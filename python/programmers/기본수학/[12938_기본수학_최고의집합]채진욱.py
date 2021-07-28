import math
n = 2
s = 9

# 최고의 집합:
# 집합 원소의 개수가 n 개이고,
# 집합의 원소의 합이 s 인 것 중에
# 원소들의 곱이 가장 큰 집합
# 최고의 집합 없으면 [-1]

# combination으로 풀면 시간 초과 무조건 일듯

# 나는 못풀었다...


# key 포인트:
# 숫자 s를 자연수 n 개로 표현하면서
# '곱이 가장 큰 수' 가 되도록 하려면,
# n 개의 각 자연수 간 차이가 가장 적어야 한다.

def solution(n, s):  # https://inspirit941.tistory.com/101
    # 자연수 n개의 합으로 n보다 작은 s를 만들 수는 없으므로 [-1]을 리턴한다
    if n > s:
        return [-1]
    result = []
    # s를 n으로 나눈 몫이 n개이도록 초기값을 정한다.
    initial = s // n
    for _ in range(n):
        result.append(initial)
    idx = len(result) - 1
    # s를 n으로 나눈 몫에서 나머지만큼 각 값에 1씩 더해준다.
    for _ in range(s % n):
        result[idx] += 1
        idx -= 1
    return result
