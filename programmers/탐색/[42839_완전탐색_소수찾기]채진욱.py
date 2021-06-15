from itertools import permutations
from math import sqrt

numbers = "17"


def prime_check(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, int(sqrt(number)+1)):
            if number % i == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    num_list = list(numbers)
    check_list = []
    for i in range(1, len(num_list)+1):
        for j in permutations(num_list, i):
            check_list.append(int(''.join(j)))
    check_list = set(check_list)
    print(check_list)

    for i in check_list:
        if prime_check(i):
            answer += 1

    return answer



print(solution(numbers))
print(prime_check(111))
