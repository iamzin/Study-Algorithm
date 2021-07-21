def solution(number, k):
    answer = ''
    
    stk=[]
    #순차 조회
    for n in number: 
        #현재 숫자가 스택 맨 위에 있는 숫자보다 작거나 같을 때까지 pop한다.
        while stk and k>0 and stk[-1]<n:
            k-=1
            stk.pop()
            
        #pop이 끝났으면, 현재 숫자를 push한다.
        stk.append(n)
        
    for n in stk:
        answer+=n
    return answer