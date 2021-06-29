phone_book = ["123", "1", "234", "345"]

# 해쉬는 key-value
# 파이썬에서는 딕셔너리
# 시간복잡도 검색: o(1)

# 번호를 key로 저장
# value는 boolean
# 각 번호를 조회할때
# startswith 사용
# 접두어인 경우 있으면 return False


def solution(phone_book):  # 시간복잡도 O(n^2) # 정확성은 통과

    for i in range(0, len(phone_book)):
        cnt = 0
        for j in phone_book:
            if phone_book[i].startswith(j):
                cnt += 1
                if cnt >= 2:
                    return False

    return True

# 해쉬 테이블 만들어 풀이
def solution2(phone_book):
    dict = {}

    for phone in phone_book:
        dict[phone] = 1

    for phone in phone_book:
        str = ""
        for i in range(len(phone)):
            str += phone[i]
            if str in dict and str != phone: # 이 부분을 생각 못함
                return False
            
    return True


# sort하고 그냥 현재 번호와 그 다음 번호와 startswith로 비교
def solution3(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


print(solution3(phone_book))
