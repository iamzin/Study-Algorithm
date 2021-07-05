# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 진법 변환하기(2~16) - 인터넷에서 주워옴..
NOTATION = '0123456789ABCDEF'


def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

# # 패턴 찾기 -> 실패


# def test(n):
#     answer = numeral_system(n, 2)
#     return answer


# for i in range(1, 21):
#     print(str(i)+'는 '+test(i))

# 본 코드


def solution(n):
    answer = 0
    one_cnt = numeral_system(n, 2).count('1')
    for i in range(n+1, 1000001):  # 범위는 2n+1까지만 잡아줘도 된다고 함 -> break문 때문에 상관없긴 할듯
        if one_cnt == numeral_system(i, 2).count('1'):
            answer = i
            break
    return answer


print(solution(15))
print(solution(78))

# 다른사람 풀이보니 bin이라는 함수가 있었음 -> 2진법 변환


def solution(n):
    answer = 0
    one_cnt = bin(n).count('1')
    for i in range(n+1, 1000001):
        if one_cnt == bin(i).count('1'):
            answer = i
            break
    return answer


# oct()  # 8진법
# hex()  # 16진법
# format(value, 진법)도 있음

print(solution(15))
print(solution(78))
