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