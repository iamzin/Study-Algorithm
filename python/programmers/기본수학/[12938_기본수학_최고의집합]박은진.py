def solution(n, s):
    answer = []
    
    if s // n < 1:
        answer = [-1]
    
    else:
        q = s // n
        for i in range(n):
            answer.append(q)
        
        r = s % n
        idx = len(answer) - 1
            
        for i in range(r):
            answer[idx-i] = answer[idx-i] + 1
                
        return answer

# https://somjang.tistory.com/entry/Programmers-%EC%B5%9C%EA%B3%A0%EC%9D%98-%EC%A7%91%ED%95%A9-Python