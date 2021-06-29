import functools
from itertools import combinations, permutations

numbers = [6, 10, 2]  # 12,1,10,110 // 12,1,110,10

# 9, 8, 13, 54, 77 -> 98775413 // 9,8,77,54, 13
# 10, 22, 3, 1, 54, 13 -> 54,3,22,13,1,10
# 1, 10, 13, 15, 120 -> 1,15,13,120,10
# 113, 120, 115, 1, 18 -> 1,18,120,115,113 // 18,120,115,113,1
# 3, 30, 34, 5, 9 -> 9,5,34,3,30

# 1, 101, 100 -> 1, 101, 100


def solution(numbers):  # permutation 쓰면 될듯 -> 시간 초과 -> permutation 시간복잡도 O(n!) -> 정렬 방법으로는 최악임
    str_numbers = list(map(str, numbers))
    str_num_list = list(
        map(''.join, permutations(str_numbers, len(str_numbers))))

    num_list = sorted(list(map(int, str_num_list)))

    return str(num_list[-1])


# 각 수의 앞자리 숫자가 큰 순으로 정렬
# 앞 자리 숫자가 같은 경우에는 그 다음 자리 숫자 큰 순서대로 정렬
def solution2(numbers):
    str_numbers = list(map(str, numbers))
    # 세 자리 이상의 수로 만들어주기 위해 x*3 # 아스키 코드 순으로 내림차순 정렬
    str_numbers.sort(key=lambda x: x*3, reverse=True)

    # int로 변환한 뒤, 또 str로 변환해주는 이유? 모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.
    return str(int("".join(str_numbers)))


# print(solution2(numbers))


# cmp_to_key을 활용한 방법 # 사용자 지정 함수를 key로 해서 정렬 # https://wikidocs.net/109303
def comparator(a, b):
    print("a: ", a)
    print("b: ", b)
    t1 = a+b
    t2 = b+a
    print((int(t1) > int(t2)) - (int(t1) < int(t2)))
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution3(numbers):
    n = [str(x) for x in numbers]
    print(n)
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


# print(comparator("100", "101"))
print(solution3(numbers))
