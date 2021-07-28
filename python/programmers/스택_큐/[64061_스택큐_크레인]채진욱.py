board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


# board를 각 열에 대한 스택들로 만들고
# 나머지 하면 간단할듯..?


def solution(board, moves):
    answer = 0
    map_stack_list = [[] for i in range(len(board))]
    result_stack = []

    # board를 각 열에 대한 스택으로 만들기  # map_stack_list: [[3, 4], [5, 2, 2], [1, 4, 5, 1], [3, 4], [1, 2, 1, 3]]
    for i in range(len(board)-1, -1, -1):
        for j in range(0, len(board)):
            if board[i][j] != 0:
                map_stack_list[j].append(board[i][j])

    for i in moves:
        if len(map_stack_list[i-1]) != 0:  # i-1에 해당하는 열에 인형이 남아있다면
            if len(result_stack) == 0:  # 바구니가 비어있다면
                # 바구니에 그냥 바로 인형을 집어넣음
                result_stack.append(map_stack_list[i-1].pop())
            # 바구니 맨 위 인형과 i-1에 해당하는 열의 맨 위 인형이 같다면
            elif result_stack[-1] == map_stack_list[i-1][-1]:
                result_stack.pop()
                map_stack_list[i-1].pop()
                answer += 2
            else:  # 바구니 맨 위 인형과 i-1에 해당하는 열의 맨 위 인형이 같지 않다면
                result_stack.append(map_stack_list[i-1].pop())

        print("map_stack_list", map_stack_list)
        print("result_stack", result_stack)

    return answer

# 튜터님 풀이


def solution2(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        index = move - 1
        for row_info in board:
            if row_info[index] != 0:
                bucket.append(row_info[index])
                row_info[index] = 0
                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    answer += 2
                    bucket = bucket[0:-2]
                break
    return answer


print(solution(board, moves))
