def solution(n):
    answer = n
    res = check(answer) # res = 1의 개수
    
    while(1):
        answer += 1 # 10진수일 때 +1
        if check(answer) == res: # 10진수일 때 +1한 값의 2진수가 res(1의 개수)랑 같은지 확인
            break # 같으면 빠져나와 return
    
    return answer

def check(n):
    return list(bin(n)).count('1') # 2진수를 list로 캐스팅하여 1의 개수 카운팅


# [재승] bin, oct, hex 쓰면 print 되는 string 값에 접두어 0b, 0o, 0x가 붙어서
# 만약 이 문제가 0을 카운팅하는 거였다면, 위 코드가 틀림
# 접두어 제거 과정을 추가해야 함: format 내장 함수 활용
# https://brownbears.tistory.com/467