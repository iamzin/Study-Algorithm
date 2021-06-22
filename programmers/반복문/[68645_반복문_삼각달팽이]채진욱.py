# 이차원배열 n 개 만큼 리스트를 만들고
# 반복문을 써서
# 리스트에 0으로 초기화 되어있는 값들을 바꿔줌

# n , n-1, n-2, n-3, n-4 ... 1 까지 반복


# n이 짝수일때, 홀수일때
# 짝수이면 세로줄은 짝수, 가로줄은 홀수
# 홀수이면 세로줄은 홀수, 가로줄은 짝수
def solution(n):
    answer = []
    stair_list = [[0]*i for i in range(1, n+1)]

    max_num = 0  # 마지막으로 나오는 숫자

    for i in range(1, n+1):
        max_num += i

    return answer


# 좌표로 생각하기
def solution2(n):
    answer = [[0]*i for i in range(1, n+1)]

    x, y = -1, 0  # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1  # 대입 숫자

    for i in range(n):  # 0부터 시작하는 회차
        for j in range(i, n):  # i 방향 회차에 대한 숫자 대입 횟수
            if i % 3 == 0:  # 회차 % 3 == 0이면 아래로 향함
                x += 1
            elif i % 3 == 1:  # 회차 % 3 == 1이면 오른쪽으로 향함
                y += 1
            else:  # 둘 다 아니면 위로 향함
                x -= 1
                y -= 1
            answer[x][y] = num
            print("x,y", x, y)
            print("answer[x][y]", answer[x][y])
            print("answer", answer)
            num += 1
    # 이중 리스트 flatten하게 만들기  #참고 https://blog.winterjung.dev/2017/04/21/list-of-lists-to-flatten
    return sum(answer, [])


print(solution2(5))
