# 땅따먹기
# 땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고,
# 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때,
# 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
# 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

# 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.

# def solution(land):

#     answer = 0
#     N = len(land)  # N은 행의 개수가 된다.
#     num = 5  # 첫 행에서는 num 이 영향을 미치면 안되므로 열의 총 수인 4보다 큰 5를 대입해놓았다.

#     for i in range(0, N):  # 0번째 행부터 N-1행까지 반복
#         max = 0
#         for j in range(0, 4):  # 각 행의 열들을 반복
#             if num == j:  # 바로 직전의 행과 같은 열을 밟을 수 없다.
#                 continue
#             if land[i][j] > land[i][max]:
#                 max = j  # 각 열에서 최대값을 찾기
#         answer += land[i][max]  # 최대값들 더해주기
#         num = max  # 이번 행에서 최대였던 열을 저장하여 다음 행에 영향을 준다.

#     return answer

def solution(land):

    answer = 0

    N = len(land)  # N은 행의 개수가 된다.
    for i in range(0, N-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
    # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
    # N-1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다.
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    # 바로 위에 코드가 똑같은 코드다. N-1행에서의 최대값을 가지는 열 answer에 대입한다.
    # print(land)
    answer = max(land[N-1])

    # answer = max(land[N-1][0],land[N-1][1],land[N-1][2],land[N-1][3])

    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
