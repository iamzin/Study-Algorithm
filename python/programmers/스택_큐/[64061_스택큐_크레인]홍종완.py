# 크레인 인형뽑기 게임 - 스택 / 큐 - 64061
def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        idx = m - 1  # move -> 1~5, board 의 인덱스 -> 0~4
        for i in board:
            if i[idx] != 0:
                stack.append(i[idx])  # 0이 아니면 스택에 넣고
                i[idx] = 0  # 0으로 초기화
                # 스택의 최상단 두개의 값이 같으면
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    answer += 2
                    stack.pop()
                    stack.pop()
                break

    return answer


# test case
b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
m = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(b, m))
