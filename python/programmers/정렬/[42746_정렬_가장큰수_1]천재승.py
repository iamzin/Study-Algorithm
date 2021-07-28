
# python2.X까지만 cmp 사용 가능
# python3.X부터 cmp 매개변수 제거, 대신 cmp_to_key()함수가 표준 라이브러리의 functools 모듈에 추가 

# 출처: https://comdoc.tistory.com/entry/7-가장-큰-수
# 출처: https://docs.python.org/ko/3/howto/sorting.html

from functools import cmp_to_key

def solution(numbers):
    answer = ''
    numbers_str=list(map(str, numbers))
    # 첫 번째가 두 번째보다 작으면(less-than) 음수 값을 반환하고, 같으면 0을 반환하고, 크면(greater-than) 양수 값을 반환해야 합니다.
    def compare(x, y): 
        if x+y>y+x:
            return -1
        elif x+y==y+x:
            return 0
        else: 
            return True

    # sort는 리스트만 가능
    # sorted는 iterator(list, dict, set, str, bytes, tuple, range) 가능
    numbers_str.sort(key=cmp_to_key(compare))
    
    # int로 변환하지 않으면 예외가 생긴다.
    # ''.join(["0","0","0","0"])="0000" 
    # ->int("0000")=0
    # ->str(0)="0"
    answer=str(int(''.join(numbers_str)))

    return answer

print(solution([3, 30, 34, 5, 9]))



