# 가장 큰 수 - 정렬 - 42746

# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 순열 - all 시간 초과

# from itertools import permutations


# def solution(numbers):
#     answer = ''
#     per_arr = list(permutations(numbers, len(numbers)))

#     for i in per_arr[0]:
#         answer += str(i)

#     for i in range(len(per_arr)):
#         temp = ''
#         for j in per_arr[i]:
#             temp += str(j)
#             if int(answer) < int(temp):
#                 answer = temp

#     return answer

# def solution(numbers):
#     answer = ''

#     numbers = list(map(str, numbers))

#     for j in range(9, -1, -1):
#         for i in numbers:
#             for k in range(0, len(i)):
#                 # print('자릿수')
#                 # print(int(i[k]))
#                 # print('숫자')
#                 # print(j)
#                 if int(i[k]) == j:
#                     answer += i
#                     break
#     # print(answer)
#     return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)

    return str(int(''.join(numbers)))  # [0,0,0,0] 인 경우

# 다른사람 풀이.
# 문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교
# 물론 같으면, 다음 인덱스도 비교. 비교한 결과 [6, 2, 10]의 순으로 정렬


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
