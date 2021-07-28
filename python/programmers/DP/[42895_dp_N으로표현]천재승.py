# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.
# 입출력 예
# N	number	return
# 5	12	4
# 2	11	3


def solution(N, number):
    answer = -1
    #dp[i]는 N을 i개로 만들 수 있는 수의 집합
    #dp[i]는dp[i-j] 집합에 있는 수와 dp[j] 집합에 있는 수를 연산에 나오는 수의 집합
    dp=[0]
    
    
    #최솟값이 8보다 크면 -1을 return하므로
    #i가 8이 될 때까지 dp[i]에 number가 있는지 확인하고 없으면 -1을 리턴한다.
    
    for i in range(1,9):
        setOfOperation=set()
        
        all_n=int(str(N)*i)
        setOfOperation.add(all_n)
        
        for j in range(1,i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    setOfOperation.add(num1+num2)
                    setOfOperation.add(abs(num1-num2))
                    setOfOperation.add(num1*num2)
                    if num2!=0:
                        setOfOperation.add(num1//num2)
        
        dp.append(setOfOperation)
        
        #i개의 N으로 표현할 수 있는 수가 있는지 집합을 확인한다.
        for num in setOfOperation:
            if num==number: 
                return i

    # print(dp)
    
    #i=8이 될 때까지 number을 찾지 못하면 -1을 반환한다.
    return answer