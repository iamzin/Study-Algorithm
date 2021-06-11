# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]



def solution(prices):
    t= len(prices) 
    st=[] 
    answer=[0]*t
    #0~t초
    for i in range(t): 
        # i초에 주식가격이 떨어졌다면
        while st and prices[st[-1]] > prices[i]: 
             
            top=st.pop()
            answer[top]=i-top #유지시간=현재시간-시작시간
        
        st.append(i)
    #스택에 남아있는 값들은 끝(t초)까지 주식가격이 떨어지지 않음
    while st : 
        top=st.pop()
        answer[top]=t-1-top
    return answer