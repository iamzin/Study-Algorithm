# 카펫 - 완전탐색 - 42842
# 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 생각 안하고 풀기
def solution(brown, yellow):
    answer = []

    total = brown + yellow
    total_sqrt = int(total ** 0.5)
    # 정사각형
    if total_sqrt**2 == total:
        answer.append(total_sqrt)
        answer.append(total_sqrt)

    # 세로보다 가로가 길 경우
    if total_sqrt**2 < total:
        answer.append(total//total_sqrt)
        answer.append(total_sqrt)

    return answer


# 맞는것 같은데 반례를 못찾겠음
#                            (테두리 4개 + 기둥*줄의 개수)
# 노란색 한줄 -> 갈색 = 노란색*2 + (4+2)
# 노란색 두줄 -> 갈색 = 노란색*1 + (4+2*2)
# 노란색 세줄 -> 갈색 = 노란색*2/3 + (4+2*3)
# 노란색 네줄 -> 갈색 = 노란색*2/4 + (4+2*4) ...

def solution(brown, yellow):
    answer = []
    total = brown + yellow

    yellow_arr = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_arr.append(i)
    # print(yellow_arr)

    yellow_line = 0
    # 노랑 몇줄 인지.
    for i in range(len(yellow_arr)):
        for j in range(1, len(yellow_arr)+1):
            if brown == yellow_arr[i]*2/j + (4+2*j):
                yellow_line = j
    # print(yellow_line)

    a = int(total/(yellow_line+2))
    b = yellow_line+2
    if a > b:
        answer.append(a)
        answer.append(b)
    else:
        answer.append(b)
        answer.append(a)

    return answer


# [4,3]
print(solution(10, 2))
# [3,3]
print(solution(8, 1))
# [8,6]
print(solution(24, 24))
# [8,3]
print(solution(18, 6))
