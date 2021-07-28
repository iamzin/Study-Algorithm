# 짝지어 제거하기 - 스택/큐 - 12973

# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.


# 제일 처음 들어간 b가 나중에 만나는 b와 만나 없어질 수 있음
# 들어간 대로 나오는 것이 아니므로 스택 이용

# 틀린 코드
# def solution(s):
#     answer = 1

#     # 홀수면 수행 불가
#     if len(s) % 2 == 1:
#         return 0

#     stack = []
#     for i in range(len(s)):
#         if s[i] == s[i-1]:
#             stack.append(s[i])
#             stack.append(s[i-1])
#             break

#     s = s[:i-1] + s[i+1:]

#     if stack == []:
#         answer = 0

#     while stack:
#         stack.pop()
#         stack.pop()
#         for i in range(len(s)):
#             if s[i] == s[i-1]:
#                 stack.append(s[i])
#                 stack.append(s[i-1])
#             break
#         s = s[:i-1] + s[i+1:]

#     return answer


def solution(s):
    stack = []
    # 홀수면 수행 불가
    if len(s) % 2 == 1:
        return 0

    for i in s:
        if len(stack) == 0:  # if not stack:
            stack.append(i)
        else:  # if stack:
            if(stack[-1] == i):  # 같으면
                stack.pop()  # pop
            else:  # 다르면 append
                stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution('baabaa'))
print(solution('cdcd'))
