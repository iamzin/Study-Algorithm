# 튜플 - 문자열 - 64065
# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# s의 길이는 5 이상 1,000,000 이하입니다.
# s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
# 숫자가 0으로 시작하는 경우는 없습니다.
# s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
# s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
# return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.

def solution(s):
    answer = []
    s = s.replace('{{', "")
    s = s.replace('}}', "")
    arr = s.split('},{')
    # s.lstrip('{').rstrip('}').split('},{') 이런 파싱법도 있다.
    # 정규식으로 하는 풀이도 있더라.

    # remind! : sort(key = len)을 이용하여 길이에 따른 정렬이 가능하다.
    arr.sort(key=len)

    for i in arr:
        temp = i.split(',')  # ,로 다시 split하고
        for t in temp:
            if int(t) not in answer:  # 정수형으로 바꾼 것들이 answer에 없을경우
                answer.append(int(t))  # answer에 대입해준다

    return answer


s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

print(solution(s1))
print(solution(s2))
