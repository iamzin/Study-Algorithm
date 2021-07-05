
# s에 있는 집합을 길이 순으로 정렬하고
# 정렬 필요 없을 수도 -> 그냥 가장 길이 긴 집합을 리스트화 하면 끝

# 구현 포인트는 문자열 s에 있는 집합들을 어떻게 나눠서 표현할것인가

# 먼저 strip 으로 {} 제거
# , 으로 split
# 길이 max 값 가져온다.

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

# 내 풀이 => 너무 길다.
# 한눈에 보기 어렵다.


def solution(s):
    answer = []
    tup_list = []
    final_list = []
    temp = ""

    s = "{" + s.lstrip("{").rstrip("}") + "}"

    # ['{2}', '{2', '1}', '{2', '1', '3}', '{2', '1', '3', '4}']
    tup_list = s.split(",")

    for i in tup_list:
        if '{' in i and '}' in i:
            final_list.append(i)
        elif '{' in i and '}' not in i:
            temp = temp + i + ','
        elif '{' not in i and '}' in i:
            temp += i
        else:
            temp = temp + i + ','
        if '{' in temp and '}' in temp:
            final_list.append(temp)
            temp = ""

    # ['{2}', '{2,1}', '{2,1,3}', '{2,1,3,4}']
    final_list.sort(key=lambda x: len(x))

    for tup in final_list:
        for j in tup:
            if j.isdigit():
                temp += j
            elif (j == ',' or j == '}') and int(temp) not in answer:
                answer.append(int(temp))
                temp = ""
            else:
                temp = ""

    return answer


# 훨씬 간단하고 이해하기 쉬운 풀이
def solution2(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')  # split('},{') => 이걸 생각 못함
    # s[2:-2].split("},{") 이것도 가능
    print("s1: ", s1)

    new_s = []
    for i in s1:
        new_s.append(i.split(','))  # 이것도 생각 못함

    new_s.sort(key=len)
    print("new_s: ", new_s)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


print(solution2(s))
