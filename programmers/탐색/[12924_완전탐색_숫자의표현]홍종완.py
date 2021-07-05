# 숫자의 표현 - 완전탐색 - 12924
# 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

# 완탐 문제라서 생각 안하고 완탐으로 품..
def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        while temp < n:
            temp += i
            i += 1
        if temp == n:
            answer += 1

    return answer


print(solution(15))
