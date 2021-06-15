# 이분탐색 - 순위 검색 - 72412
# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,
# 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
# 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

def solution(info, query):
    answer = []
    new_query = []
    for i in query:
        new_query.append(i.replace(" and", ""))
    print(new_query)

    # 점수 조건 먼저 구해놓고 새로운 배열에 Info 와 쿼리를 넣는다.
    # 나머지는 쿼리와 비교해서 같으면 cnt + 1(or - 포함)

    for i in range(len(query)):
        cnt = 0
        for j in range(len(info)):
            print('info는')
            print(info[j].split()[-1])
            print('query는')
            print(new_query[i].split()[-1])
            if (info[j].split()[-1] >= new_query[i].split()[-1]):
                cnt += 1
            print('cnt는')
            print(cnt)
        answer.append(cnt)

    return answer


# test case -> [1,1,1,1,2,4]
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

# print(info[0].split())
# print(query[0].split(" and "))
# print(query[0].split("and")[-1].split()[0])
print(solution(info, query))
