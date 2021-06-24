def solution(numbers):
    answer = ''
    numbers_str=list(map(str, numbers))

    #문자 조건: 길이 1000이하
    numbers_str.sort(key=lambda number: number*3, reverse=True)

    
    # int로 변환하지 않으면 예외가 생긴다.
    # ''.join(["0","0","0","0"])="0000" 
    # ->int("0000")=0
    # ->str(0)="0"
    answer=str(int(''.join(numbers_str)))

    return answer

print(solution([3, 30, 34, 5, 9]))