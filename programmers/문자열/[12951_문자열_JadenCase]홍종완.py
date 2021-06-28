# JadenCase 만들기 - 문자열 - 12951
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# s는 길이 1 이상인 문자열입니다.
# s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

# 신경써야할 것 - 공백이 연속된 경우, 단어의 시작이 숫자인 경우

# 실패코드 - continue 안쓰고.. -> 연속된 공백일 경우 - 공백 하나 더 붙음

# def solution(s):
#     answer = ''

#     s = s.lower()
#     if s[0].islower():
#         s = s[0].upper() + s[1:]

#     for i in range(len(s)):
#         if s[i-1] == " " and s[i].islower():
#             continue
#         if s[i-1] == " " and s[i].isdecimal():
#             continue
#         answer += s[i]
#         if s[i] == " ":
#             answer += s[i+1].upper()

#     return answer

# continue로 처리 - 성공
def solution(s):
    answer = ''
    # 모두 소문자로
    s = s.lower()
    # 첫번째 글자
    if s[0].islower():
        s = s[0].upper() + s[1:]

    for i in range(len(s)):
        # 이전 인덱스의 값이 공백이면서 현재 인덱스의 값이 소문자인경우
        if s[i-1] == " " and s[i].islower():
            answer += s[i].upper()
            continue
        # 나머지는 그대로 붙여준다
        answer += s[i]

    return answer

# split 써서 리스트 <-> 문자열로 푸는 방법도 있을 것 같다
# def solution(s):
#     answer = ''

#     s = s.split(" ")
#     print(s)

#     return answer


print(solution("3people unFollowed me"))
print(solution('for the last week'))
print(solution("test case  dldldl"))
print(solution('for 3the 3last 3week'))
