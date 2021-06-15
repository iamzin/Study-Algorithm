import math
from itertools import permutations

#소수 찾기
def isPrime(num):

    if num==0 or num==1:
        return False
    
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i ==0:
                return False
        return True

def solution(numbers):
    answer=[]
    for i in range(1, len(numbers)+1):
        arr= list(permutations(numbers, i)) 
        for j in range(len(arr)):
            num=int(''.join(map(arr[j])))
            if isPrime(num):
                answer.append(num)

    answer=list(set(answer))
    return len(answer)

print(solution("011"))