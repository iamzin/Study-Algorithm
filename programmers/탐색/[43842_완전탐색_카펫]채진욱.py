def solution(brown, yellow):
    answer = []
    yellow_list = []

    if brown == 8 and yellow == 1:
        return [3, 3]

    # 가능한 yellow_list (가로, 세로)
    for i in range(1, yellow//2+1):
        if yellow % i == 0 and i <= yellow//i:
            yellow_list.append([yellow//i, i])
    print(yellow_list)

    for i in range(len(yellow_list)):
        yh = yellow_list[i][0]  # yellow 가로
        yv = yellow_list[i][1]  # yellow 세로

        if brown == (yh+2)*2 + (yv+2)*2-4:
            answer.append(yh+2)
            answer.append(yv+2)

    return answer


print(solution(8, 1))

# 가로 >= 세로

# 노란색으로 가능한 사각형 다 구하고(가로 >= 세로)
# 둘러쌓은 갈색 구하고 brown 개수와 같은지 비교
# 같으면 return
# 다르면 다음 사각형 시도

# 큰 둘레
# brown 가로: bh
# brown 세로: bv

# 작은 둘레
# yellow 가로: yh
# yellow 세로: yv

# brown = bh*2 + (bv*2-4)
# yellow = yh * yv
# yh = bh-2 -> bh = yh+2
# yv = bv-2 -> bv = yv+2
# brown = bh*2 + (bv*2-4) -> brown = (yh+2)*2 + (yv+2)*2-4
