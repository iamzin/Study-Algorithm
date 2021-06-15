n = 6
dp = [0] * 60000
dp[1] = 1
dp[2] = 2


# 내가 푼 방식
def solution(n):  # DP로 품 (메모이제시연 바텀업 방식)

    if n == 1 or n == 2:
        return dp[n]

    for i in range(3, n+1):
        # 연산하는 수가 커지면 오래 걸리기 때문에 마지막 return할때 나머지 연산을 하지 말고
        # 더할 때 마다 나머지 연산을 해야 효율성 시간초과가 안뜸
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007

    return dp[n]


# 다른 사람 풀이
# 리스트도 사용안하고 바로 품
# 내 풀이 대비 시간 2배 이상 빠름
def solution2(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b


# 재귀 풀이 (런타임에러: 시간 초과)
def recursion(n):
    if n == 1 or n == 2:
        return dp[n]

    if dp[n] != 0:
        return dp[n]

    dp[n] = recursion(n-1)+recursion(n-2)
    return dp[n] % 1000000007


print(solution(n))
# print(recursion(n))
