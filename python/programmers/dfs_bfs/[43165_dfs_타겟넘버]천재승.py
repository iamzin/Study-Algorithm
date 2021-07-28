def solution(numbers, target):
    answer = 0
    
    #비트연산 00..0~11..1을 확인한다.
    #0이 나오면 -, 1이 나오면 + 연산한다. 
    
    for i in range(0, 1<<len(numbers)): 
        sum= 0
        for j in range(0,len(numbers)):
            #숫자의 이진수를 확인한다.
            if i & (1<<j): 
                sum+=numbers[j]
            else: 
                sum-=numbers[j]
        
        if sum==target:
            answer+=1
    
    
    return answer