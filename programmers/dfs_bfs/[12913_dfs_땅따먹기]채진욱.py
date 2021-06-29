land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

# dfs
# 스택 또는 재귀함수 활용

# ** 이 문제에서 dfs나 단순 for문으로 풀이하면 시간 초과 발생


# 동적계획법 풀이
def solution(land):
    n = len(land)-1
    for i in range(n):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[n][0], land[n][1], land[n][2], land[n][3])


# 동적계획법2 -> 더 파이썬 다운 풀이
def solution2(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 현재 land[i][j]에 그 윗 행의 j이전 까지의 요소들과 j 이후의 요소들 중 가장 큰 값을 구하고
            # 현재 요소 값을 더한 누적 값을 나타낸다.
            land[i][j] = max(land[i - 1][: j] + land[i - 1]
                             [j + 1:]) + land[i][j]
    return max(land[-1])


solution(land)
