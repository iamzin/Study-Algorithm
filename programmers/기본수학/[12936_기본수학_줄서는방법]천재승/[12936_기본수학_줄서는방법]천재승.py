import math

def solution(n, k):
    answer = []
    #1~n번호 리스트
    numbers=[i+1 for i in range(n)]

    #문제의 k번째 방법은 1번째를 시작으로 카운트된 방법
    #1번째부터 시작은 index가 0번부터 시작되는 것과 혼동이 있으므로
    #혼동을 피하고자 자체적으로 k-=1해서 코드 상으로는 0번째부터 시작하는 k-1번째 방법을 찾는다.
    k-=1

    #앞자리에 나올 번호 추출을 반복한다.
    #추출할 번호가 없음은 나열이 끝남을 의미한다.
    while len(numbers)!=0 : 
        
        #각 사람이 첫 번째에 올 경우 경우의 수
        temp=math.factorial(len(numbers)-1)

        #그 다음 앞에 위치할 번호의 index 계산
        idx=k//temp
        
        k=k%temp

        
        answer.append(numbers.pop(idx))
  
        
        
     
    return answer


print(solution(3,2))