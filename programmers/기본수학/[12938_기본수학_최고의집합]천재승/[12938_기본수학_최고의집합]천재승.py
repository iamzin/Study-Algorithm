def solution(n, s):
    answer = []
    
    #고르게 분포될 값을 구한다.
    a=s//n
    if a==0:
        return [-1]
    #남은 값은 뒤에서 앞으로 1씩 뿌려준다.
    b=s%n
    
    for i in range(n):
        answer.append(a)
        
    for i in range(b):
        answer[n-1-i]+=1
        
    return answer