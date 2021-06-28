# 전화번호 목록 - 해시 - 42577
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

def solution(phone_book):
    answer = True
    # 정렬 시키고,
    phone_book.sort()

    for s1, s2 in zip(phone_book, phone_book[1:]):
        # 이전 원소의 len 만큼 다음 원소와 s1을 비교
        # startswith 라는 거 이용 가능하다고함
        if s1 in s2[:len(s1)]:
            answer = False
    return answer


print(solution(["119", "97674223", "1195524421"]))


# 해시 이용 풀이


def solution(phone_book):

    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # print(temp)
            if temp in hash_map and temp != phone_number:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
