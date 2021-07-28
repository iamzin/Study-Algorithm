# 지수 구하기 - 지수 이용할 수 있지 않을까 해서 해봄
# def binary_test(n):
#     cnt = 0
#     while n >= 2:
#         cnt += 1
#         n = n/2
#     return cnt

# # 의식의 흐름, 실패
# def solution(n, a, b):
#     cnt = 0

#     while n > 2:
#         # 홀수로 만들기
#         if a % 2 == 0:
#             a -= 1
#         if b % 2 == 0:
#             b -= 1
#         # 비교할 중앙값
#         mid = int(n/2)
#         # 부호가 다르면
#         if (mid-a) * (mid-b) < 0:
#             cnt += 1
#         elif (mid-a) * (mid-b) > 0 and abs(b-a) == int(mid/2):
#             cnt += 1
#         a = int((a+1)/2)
#         b = int((b+1)/2)
#         n = int(n/2)

#     return cnt+1


def solution(n, a, b):

    answer = 1
    while True:
        # a가 짝수고 a-1 = b 이거나, a가 홀수고 a+1 =b 이면 return
        if (a % 2 == 0 and a - 1 == b) or (a % 2 != 0 and a + 1 == b):
            return answer

        # 승리 조건
        if a % 2 == 0:
            a = int(a / 2)  # 짝수면 2로 나눔
        else:
            a = int((a / 2) + 1)  # 홀수면 2로 나누고 +1

        if b % 2 == 0:
            b = int(b / 2)
        else:
            b = int((b / 2) + 1)

        answer += 1  # 한바퀴 추가

# print(solution(8, 4, 7))
# # print(solution(8, 4, 5))
# print(solution(8, 1, 2))
# print(solution(8, 2, 3))
# for i in range(1, 8):
#     print(solution(8, i, i+1))
