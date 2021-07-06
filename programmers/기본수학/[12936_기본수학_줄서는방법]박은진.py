from math import factorial

def solution(n, k):
    answer = []
    nums = list(range(1, n+1))

    # n=3, k=5
    while (n != 0):                             # (1)
        temp = factorial(n-1)                   # 2! = 2x1 = 2
        answer.append(nums.pop((k-1)//temp))    # 4//2 -> nums[2] -> 3
        n -= 1                                  # n = 2
        k %= temp                               # 5%2 -> 1

    return answer